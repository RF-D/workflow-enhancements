# iTerm Alias Setup Instructions

This guide will walk you through the process of integrating custom aliases into your iTerm environment to streamline your development workflow.

## Prerequisites

- iTerm2 installed on your macOS system

## Manual Setup Instructions

Follow these steps to manually add the provided aliases to your shell profile:

1. **Download start_sequence.scpt:**
   Download the `start_sequence.scpt` file from the repository or clone the entire repository to your local machine.

2. **Open Your Shell Profile:**
   - For Bash, open your `.bash_profile` file:
     ```bash
     open -a "TextEdit" ~/.bash_profile
     ```
   - For Zsh, open your `.zshrc` file:
     ```bash
     open -a "TextEdit" ~/.zshrc
     ```

3. **Add Aliases:**
   Copy the aliases from the "Aliases Included" section below and paste them into your shell profile file. Place them towards the end of the file or in a dedicated section for aliases to maintain organization.

4. **Update Path to start_sequence.scpt:**
   In the `dsync` alias, replace `/path/to/start_sequence.scpt` with the actual path to your `start_sequence.scpt` file that you downloaded or cloned from the repository. Make sure to provide the correct path to ensure the script is executed properly.

5. **Allow Permissions for start_sequence.scpt (if necessary):**
   

6. **Review Existing Aliases:**
   Before saving the file, review any existing aliases you might have in your profile. Modify any that conflict or are duplicated with the new aliases to suit your specific workflow needs.

7. **Save and Close:**
   Save the changes to your shell profile file and close the text editor.

8. **Apply Changes:**
   To apply the changes, source your profile file in iTerm or Terminal:
   - For Bash:
     ```bash
     source ~/.bash_profile
     ```
   - For Zsh:
     ```bash
     source ~/.zshrc
     ```

9. **Verify Installation:**
   Test the aliases in iTerm to ensure they work as expected. Simply type the alias name and press enter. For example:
   ```bash
   dsync

## Aliases Included

Here are the specific alias commands and their associated operations:

```bash
# make dev-sync alias that starts automation flow with error checks and notifications
alias dsync="git pull; if [ \$? -ne 0 ]; then osascript -e 'display notification \"git pull failed\" with title \"Error Notification\" sound name \"Basso\"'; else make dev-sync && osascript -e 'display notification \"make dev-sync has completed\" with title \"iTerm2 Notification\" sound name \"Ping\"' && sleep 1 && touch /tmp/dsync_done && /usr/bin/osascript /path/to/start_sequence.scpt; fi"

# Starts webpacker and sends a notification on termination
alias packer="make webpacker-start; osascript -e 'display notification \"webpacker-start terminated\" with title \"iTerm2 Notification\" sound name \"Ping\"'"

# Starts web server processes and notifies on termination
alias web="make web-start; osascript -e 'display notification \"web-start has terminated\" with title \"iTerm2 Notification\" sound name \"Ping\"'"

# Triggers cloudflare tunnel startup and sends a notification when it starts
alias cloud="make cloud-deploy; osascript -e 'display notification \"cloudflare tunnels have started\" with title \"Deployment Notification\" sound name \"Ping\"'"



