# iTerm Automation Script

This AppleScript automates the process of running various development commands when switching branches in iTerm. It is designed to save time and streamline the workflow by automatically executing the necessary commands and providing notifications upon completion.

## Overview

The main purpose of this script is to automate the following tasks when switching branches:

1. Run `make dev-sync` command to sync the development environment.
2. Start the `packer` command in a separate tab to build and package the application.
3. Start the `web` command in another tab to run the web server.
4. Check if the Cloudflare tunnel is already running, and if not, start the `cloud` command in a new tab to establish the tunnel.

By automating these tasks, developers can save time and focus on their core development work without manually executing each command whenever they switch branches.

## Prerequisites

- iTerm2 installed on your macOS system
- Have 4 tabs open with cf repo active 
- Complete Cloudflared tunnel setup

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

5. **Update Cloud Alias:**
   In the `cloud` alias, replace `<port>` with the appropriate port number on which your local server is running, and replace `<tunnel-name>` with the name of your Cloudflare Tunnel. For example:
   ```bash
   alias cloud="cloudflared tunnel run --url http://localhost:3000 my-tunnel"
## Aliases Included

Here are the specific alias commands and their associated operations:

```bash
# make dev-sync alias that starts automation flow with error checks and notifications
alias dsync="git pull; if [ \$? -ne 0 ]; then osascript -e 'display notification \"git pull failed\" with title \"Error Notification\" sound name \"Basso\"'; else make dev-sync && osascript -e 'display notification \"make dev-sync has completed\" with title \"iTerm2 Notification\" sound name \"Ping\"' && sleep 1 && touch /tmp/dsync_done && /usr/bin/osascript /path/to/start_sequence.scpt; fi"

# Starts webpacker and sends a notification on termination
alias packer="make webpacker-start; osascript -e 'display notification \"webpacker-start terminated\" with title \"iTerm2 Notification\" sound name \"Ping\"'"

# Starts web server processes and notifies on termination
alias web="make web-start; osascript -e 'display notification \"web-start has terminated\" with title \"iTerm2 Notification\" sound name \"Ping\"'"

# Triggers cloudflare tunnel startup 
alias cloud="cloudflared tunnel run --url http://localhost:<port> <tunnel-name>""



