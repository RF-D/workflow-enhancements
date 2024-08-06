# FeatureToggleHelper

FeatureToggleHelper is a Python tool for managing feature gates in YAML configuration files. It provides an interactive interface to view, modify, add, and remove feature gates while maintaining the original structure and categories.

## Important Note

This script is designed to work specifically on macOS with iTerm2. It may not function correctly on other operating systems or terminal emulators.

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

- macOS
- iTerm2
- Python 3.6 or higher
- PyYAML library
- termcolor library

## Installation

1. Ensure you have iTerm2 installed on your Mac. If not, download and install it from [https://iterm2.com/](https://iterm2.com/).

2. Clone this repository or download the `FeatureToggleHelper.py` file.

3. Create and activate a virtual environment (recommended):

```bash
python3 -m venv ~/featuretoggle_env
source ~/featuretoggle_env/bin/activate
```

4. Install the required libraries:

```bash
pip install PyYAML termcolor
```

5. To deactivate the virtual environment when you're done:

```bash
deactivate
```

## Usage

1. Open iTerm2 on your Mac.

2. Navigate to the directory containing `FeatureToggleHelper.py`.

3. Activate the virtual environment:

```bash
source ~/featuretoggle_env/bin/activate
```

4. Run the script:

```bash
python FeatureToggleHelper.py
```

5. When prompted, you can either:

   - Drag and drop the YAML file from your Finder into the iTerm2 window to input the file path.
   - Manually enter or paste the full path to your YAML file.

6. Follow the on-screen prompts to manage your feature gates.

7. After you're done, you can deactivate the virtual environment:

```bash
deactivate
```

## Notes

- The script is designed to work exclusively with iTerm2 on macOS. It will attempt to launch iTerm2 automatically if not already running in it.
- Ensure your YAML file follows the expected format with section headers surrounded by '#' characters.
- Feature gate names should follow the naming guidelines provided in the script.
- Remember to activate the virtual environment each time you want to use the script.
