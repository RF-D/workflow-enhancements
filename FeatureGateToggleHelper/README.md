# FeatureToggleHelper

FeatureToggleHelper is a Python tool for managing feature gates in YAML configuration files. It provides an interactive interface to view, modify, add, and remove feature gates while maintaining the original structure and categories.

## Features

- View and modify feature gates in a YAML file, preserving categories
- Add and remove feature gates (single or multiple)
- Add and remove category sections
- Select feature gates by number or cycle through them
- Support for drag-and-drop file input
- Enhanced color-coded output for better readability
- Continuous editing mode for quick toggling of feature gates
- Intuitive section selection and feature gate naming guidelines

## Requirements

- Python 3.6 or higher
- PyYAML library
- termcolor library

## Installation

1. Clone this repository or download the `FeatureToggleHelper.py` file.

2. Install the required libraries using the requirements.txt file:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the required libraries manually:

```bash
pip install PyYAML termcolor
```

## Usage

1. Open a terminal and navigate to the directory containing `FeatureToggleHelper.py`.

2. Run the script:

```bash
python FeatureToggleHelper.py
```

3. When prompted, you can either:

   - Drag and drop the YAML file from your file explorer into the terminal to input the file path.
   - Manually enter or paste the full path to your YAML file.

4. Follow the on-screen prompts to manage your feature gates.

## Notes

- The script is designed to work best with iTerm on macOS. If not running in iTerm, it will attempt to launch iTerm automatically.
- Ensure your YAML file follows the expected format with section headers surrounded by '#' characters.
- Feature gate names should follow the naming guidelines provided in the script.
