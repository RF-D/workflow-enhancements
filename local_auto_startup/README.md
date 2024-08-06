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
alias dsync="git pull; if [ $? -ne 0 ]; then osascript -e 'display notification \"git pull failed\" with title \"Error Notification\" sound name \"Basso\"'; else bundle exec rails assets:clobber && make dev-sync && osascript -e 'display notification \"make dev-sync has completed\" with title \"iTerm2 Notification\" sound name \"Ping\"' && sleep 1 && touch /tmp/dsync_done && /usr/bin/osascript path/to/start_sequence.scpt; fi"

# Starts webpacker and sends a notification on termination
alias packer="make webpacker-start; osascript -e 'display notification \"webpacker-start terminated\" with title \"iTerm2 Notification\" sound name \"Ping\"'"

# Starts web server processes and notifies on termination
alias web="make web-start; osascript -e 'display notification \"web-start has terminated\" with title \"iTerm2 Notification\" sound name \"Ping\"'"

# Triggers cloudflare tunnel startup 
alias cloud="cloudflared tunnel run --url http://localhost:<port> <tunnel-name>"
```


## Additional Notes: Enabling iTerm2 Notifications for Automation Script

To enable notifications for the processes in the iTerm2 automation script, utilize the built-in triggers feature in iTerm2. Here's how to set up notifications for each process:

1. **Open iTerm2 Preferences**:
   - Access the Preferences from the iTerm2 menu or by pressing `Cmd + ,`.

2. **Navigate to Profiles**:
   - Go to the "Profiles" tab within the Preferences window.

3. **Select Your Profile**:
   - Choose the profile you want to modify (e.g., "Default").

4. **Access Advanced Settings**:
   - Click on the "Advanced" tab within the profile settings.

5. **Edit Triggers**:
   - Locate the "Triggers" section and click on the "Edit" button.

6. **Add New Triggers**:
   - Click the "+" button at the bottom left corner to start adding a new trigger.

7. **Configure Triggers**:
   - Set up notifications for each process as follows:
     - **For web-packer process notification**
       - **Regular Expression**: `successfully rebuilt - now reloading`
       - **Action**: Select "Run Command..."
       - **Parameters**: Enter `sleep 30 && osascript -e 'display notification "Packer has completed" with title "iTerm2 Notification" sound name "Ping"'`
       - **Instant**: Check this box to trigger the notification immediately.
     - **For web-start processes notifications:**
       - **Regular Expression**: `"backfill-events"`
       - **Action**: Select "Run Command..."
       - **Parameters**: Enter `sleep 5 && osascript -e 'display notification "web-start has completed, Local ENV is now loading" with title "iTerm2 Notification" sound name "Ping"'`
       - **Instant**: Check this box to trigger the notification immediately.

8. **Save and Close**:
   - Click on the "Close" button to save your configurations after setting up the triggers.

9. **Apply to Additional Profiles**:
   - Repeat steps 3-8 for any other profiles you want to configure.

**Outcome of Triggers**:
- **For web-packer process notification**: A notification "Packer has completed" will appear after a 30-second delay.
- **For web-start processes notifications**: A notification "web-start has completed, Local ENV is now loading" will appear after a 5-second delay.


