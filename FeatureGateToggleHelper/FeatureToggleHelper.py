#!/usr/bin/env python3
import os
import subprocess
import yaml
import sys
import re
from termcolor import colored

"""
FeatureToggleHelper: A tool for managing feature gates in YAML configuration files.

This script allows users to view, modify, add, and remove feature gates in a YAML configuration file.
It provides an interactive interface to navigate through different sections and update
feature gate values while maintaining the original structure and categories.

Features:
- View and modify feature gates in a YAML file, preserving categories
- Add and remove feature gates (single or multiple)
- Add and remove category sections
- Select feature gates by number or cycle through them
- Support for drag-and-drop file input
- Enhanced color-coded output for better readability
- Error handling for file operations and user inputs
- Handles the specific YAML structure with section headers
- Continuous editing mode for quick toggling of feature gates
- Intuitive section selection and feature gate naming guidelines
- Graceful handling of empty sections
"""


def launch_iterm():
    """Launch the script in iTerm if not already running in it."""
    if "TERM_PROGRAM" not in os.environ or os.environ["TERM_PROGRAM"] != "iTerm.app":
        script_path = os.path.abspath(sys.argv[0])
        subprocess.Popen(["open", "-a", "iTerm", script_path])
        sys.exit(0)


def get_file_path():
    """Get the YAML file path from user input, supporting drag-and-drop."""
    print(
        colored(
            "You can drag and drop the YAML file from the VS Code tab into the terminal to get the file path.",
            "cyan",
        )
    )
    file_path = input(
        colored("Alternatively, please enter the full path to the YAML file: ", "white")
    ).strip("'")

    if not os.path.isfile(file_path):
        print(colored(f"File not found: {file_path}", "red"))
        sys.exit(1)

    return file_path


def read_yaml_file(file_path):
    """Read the content of a YAML file."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except IOError as e:
        print(colored(f"Error reading file: {e}", "red"))
        sys.exit(1)


def write_yaml_file(file_path, data):
    """Write data to a YAML file, preserving the original format."""
    try:
        with open(file_path, "w") as file:
            for section, gates in data.items():
                file.write(f"{'#' * 20} {section} {'#' * 20}\n")
                for gate, value in gates.items():
                    file.write(f"{gate}: {str(value).lower()}\n")
                file.write("\n")
        print(colored("File updated successfully.", "green"))
    except IOError as e:
        print(colored(f"Error writing to file: {e}", "red"))


def parse_yaml_content(yaml_content):
    """Parse YAML content and return a structured dictionary."""
    data = {}
    current_section = None
    for line in yaml_content.split("\n"):
        if line.strip().startswith("#"):
            section_match = re.search(r"#{20}\s+(.*?)\s+#{20}", line)
            if section_match:
                current_section = section_match.group(1)
                data[current_section] = {}
        elif ":" in line and current_section:
            key, value = line.split(":", 1)
            data[current_section][key.strip()] = value.strip().lower() == "true"
    return data


def display_sections(data):
    """Display available sections in the YAML file."""
    print(colored("\nAvailable sections:", "cyan"))
    for index, section in enumerate(data.keys(), start=1):
        print(colored(f"{index}. {section}", "white"))


def display_feature_gates(section_name, feature_gates):
    """Display feature gates for a specific section."""
    separator = "=" * 50
    print(colored(f"\n{separator}", "cyan"))
    print(colored(f"Feature gates for: {section_name}", "cyan"))
    print(colored(separator, "cyan"))
    if not feature_gates:
        print(colored("No feature gates available in this section.", "yellow"))
    else:
        for index, (gate, value) in enumerate(feature_gates.items(), start=1):
            value_color = "green" if value else "red"
            print(f"{index}. {gate}: {colored(str(value).lower(), value_color)}")


def toggle_feature_gate(data, section, feature_gate):
    """Toggle the value of a feature gate."""
    data[section][feature_gate] = not data[section][feature_gate]
    return True


def format_feature_gate_name(name):
    """Format feature gate name by removing extra colons, spaces, and converting to lowercase."""
    return name.strip().strip(":").lower().replace(" ", "-")


def display_feature_gate_naming_guidelines():
    """Display guidelines for naming feature gates."""
    print(colored("\nFeature Gate Naming Guidelines:", "yellow"))
    print("1. Use lowercase letters, numbers, and hyphens.")
    print("2. Start with a letter.")
    print("3. Use hyphens to separate words.")
    print("4. Be concise but descriptive.")
    print("5. Avoid special characters other than hyphens.")
    print(
        colored(
            "Examples: 'new-feature', 'dark-mode-enabled', 'beta-test-2023'", "cyan"
        )
    )


def add_new_feature_gate(data, section):
    """Add a new feature gate to the specified section."""
    display_feature_gate_naming_guidelines()
    new_gate = format_feature_gate_name(
        input(colored("\nEnter the name of the new feature gate: ", "white"))
    )
    if not new_gate:
        print(colored("Feature gate name cannot be empty.", "red"))
        return False
    if new_gate in data[section]:
        print(
            colored(
                "This feature gate already exists. Please use the update option to modify it.",
                "red",
            )
        )
        return False
    while True:
        new_value = input(
            colored(f'Enter the value for "{new_gate}" [1=True, 0=False]: ', "white")
        )
        if new_value == "1":
            data[section][new_gate] = True
            return True
        elif new_value == "0":
            data[section][new_gate] = False
            return True
        else:
            print(
                colored(
                    "Invalid input. Please enter '1' for true or '0' for false.", "red"
                )
            )


def add_multiple_feature_gates(data, section):
    """Add multiple feature gates to the specified section."""
    display_feature_gate_naming_guidelines()
    print(
        colored(
            "\nEnter multiple feature gates in the format 'name: value' (one per line). Press Enter on an empty line to finish.",
            "cyan",
        )
    )
    while True:
        new_gate = input(colored("Feature gate (or press Enter to finish): ", "white"))
        if new_gate == "":
            break
        try:
            gate_name, gate_value = new_gate.split(":", 1)
            gate_name = format_feature_gate_name(gate_name)
            gate_value = gate_value.strip().lower()
            if not gate_name:
                print(colored("Feature gate name cannot be empty.", "red"))
            elif gate_name in data[section]:
                print(
                    colored(
                        f"Feature gate '{gate_name}' already exists. Skipping.", "red"
                    )
                )
            elif gate_value in ["true", "false"]:
                data[section][gate_name] = gate_value == "true"
                print(colored(f"Added: {gate_name}: {gate_value}", "green"))
            else:
                print(colored("Invalid value. Please enter 'true' or 'false'.", "red"))
        except ValueError:
            print(colored("Invalid format. Please use 'name: value' format.", "red"))
    return True


def add_new_section(data):
    """Add a new category section."""
    new_section = input(colored("Enter the name of the new section: ", "white"))
    if new_section in data:
        print(
            colored(
                "This section already exists. Please choose a different name.", "red"
            )
        )
        return False
    data[new_section] = {}
    print(colored(f"New section '{new_section}' added successfully.", "green"))
    return True


def remove_section(data, file_path):
    """Remove a section from the YAML file."""
    display_sections(data)
    section_choice = input(
        colored(
            "\nEnter the section number to remove (or press Enter to go back): ",
            "white",
        )
    )
    if section_choice == "":
        return
    if section_choice.isdigit() and 1 <= int(section_choice) <= len(data):
        selected_section = list(data.keys())[int(section_choice) - 1]
        confirm = input(
            colored(
                f"Are you sure you want to remove the section '{selected_section}'? (yes/no): ",
                "white",
            )
        ).lower()
        if confirm == "yes":
            del data[selected_section]
            write_yaml_file(file_path, data)
            print(
                colored(f"Section '{selected_section}' removed successfully.", "green")
            )
        else:
            print(colored("Section removal cancelled.", "white"))
    else:
        print(colored("Invalid section number. Please try again.", "red"))


def remove_feature_gate(data, section, file_path):
    """Remove a feature gate from the specified section."""
    if not data[section]:
        print(
            colored("No feature gates available to remove in this section.", "yellow")
        )
        return
    display_feature_gates(section, data[section])
    gate_choice = input(
        colored(
            "\nEnter the feature gate number to remove (or press Enter to go back): ",
            "white",
        )
    )
    if gate_choice == "":
        return
    if gate_choice.isdigit() and 1 <= int(gate_choice) <= len(data[section]):
        selected_gate = list(data[section].keys())[int(gate_choice) - 1]
        confirm = input(
            colored(
                f"Are you sure you want to remove the feature gate '{selected_gate}'? (yes/no): ",
                "white",
            )
        ).lower()
        if confirm == "yes":
            del data[section][selected_gate]
            write_yaml_file(file_path, data)
            print(
                colored(
                    f"Feature gate '{selected_gate}' removed successfully.", "green"
                )
            )
        else:
            print(colored("Feature gate removal cancelled.", "white"))
    else:
        print(colored("Invalid feature gate number. Please try again.", "red"))


def continuous_edit_mode(data, section, file_path):
    """Continuous editing mode for quick toggling of feature gates."""
    gates = list(data[section].keys())
    if not gates:
        print(
            colored(
                "No feature gates available in this section. Please add a feature gate first.",
                "yellow",
            )
        )
        return

    print(colored("Entering Continuous Edit Mode.", "green"))
    print(
        colored(
            "Commands: 'q' to quit, 'n' for next gate, 't' to toggle, or enter a gate number to select and toggle.",
            "yellow",
        )
    )
    index = 0
    while True:
        display_feature_gates(section, data[section])
        gate = gates[index]
        value = data[section][gate]
        choice = input(
            colored(f"\nCurrent gate: {gate} [{value}] (t/n/q/[gate number]): ", "cyan")
        ).lower()
        if choice == "q":
            break
        elif choice == "n":
            index = (index + 1) % len(gates)
        elif choice == "t":
            toggle_feature_gate(data, section, gate)
            write_yaml_file(file_path, data)
        elif choice.isdigit():
            gate_num = int(choice)
            if 1 <= gate_num <= len(gates):
                selected_gate = gates[gate_num - 1]
                toggle_feature_gate(data, section, selected_gate)
                write_yaml_file(file_path, data)
                index = gate_num - 1  # Update index to the selected gate
            else:
                print(colored("Invalid gate number. Please try again.", "red"))
        else:
            print(
                colored(
                    "Invalid input. Please enter 't' to toggle, 'n' for next, 'q' to quit, or a valid gate number.",
                    "red",
                )
            )


def manage_feature_gates(data, file_path):
    """Manage feature gates interactively."""
    while True:
        display_sections(data)
        print(colored("\nFeature Gate Management:", "magenta"))
        print(colored("1. Edit section", "white"))
        print(colored("2. Add new section", "white"))
        print(colored("3. Remove section", "white"))
        print(colored("4. View all feature gates", "white"))
        print(colored("5. Save and exit", "white"))

        option_choice = input(colored("\nEnter your choice (1-5): ", "cyan"))

        if option_choice == "1":
            display_sections(data)  # Show sections again
            section_choice = input(
                colored("\nEnter the section number to edit: ", "cyan")
            )
            if section_choice.isdigit() and 1 <= int(section_choice) <= len(data):
                selected_section = list(data.keys())[int(section_choice) - 1]
                modify_section(data, selected_section, file_path)
            else:
                print(colored("Invalid section number. Please try again.", "red"))
        elif option_choice == "2":
            if add_new_section(data):
                write_yaml_file(file_path, data)
        elif option_choice == "3":
            remove_section(data, file_path)
        elif option_choice == "4":
            view_feature_gates(data)
        elif option_choice == "5":
            write_yaml_file(file_path, data)
            print(colored("Changes saved. Exiting the program.", "green"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))


def modify_section(data, section, file_path):
    """Modify feature gates within a section."""
    while True:
        display_feature_gates(section, data[section])
        print(colored("\nSection Management:", "magenta"))
        print(colored("1. Edit feature gates (Continuous Mode)", "white"))
        print(colored("2. Add new feature gate", "white"))
        print(colored("3. Add multiple feature gates", "white"))
        print(colored("4. Remove feature gate", "white"))
        print(colored("5. Return to main menu", "white"))

        option_choice = input(colored("\nEnter your choice (1-5): ", "cyan"))

        if option_choice == "1":
            continuous_edit_mode(data, section, file_path)
        elif option_choice == "2":
            if add_new_feature_gate(data, section):
                write_yaml_file(file_path, data)
        elif option_choice == "3":
            if add_multiple_feature_gates(data, section):
                write_yaml_file(file_path, data)
        elif option_choice == "4":
            remove_feature_gate(data, section, file_path)
        elif option_choice == "5":
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))


def view_feature_gates(data):
    """View all feature gates in the YAML file."""
    for section, gates in data.items():
        display_feature_gates(section, gates)
    input(colored("\nPress Enter to continue...", "white"))


def main():
    """Main function to run the FeatureToggleHelper."""
    launch_iterm()
    file_path = get_file_path()
    yaml_content = read_yaml_file(file_path)
    data = parse_yaml_content(yaml_content)
    manage_feature_gates(data, file_path)


if __name__ == "__main__":
    main()
