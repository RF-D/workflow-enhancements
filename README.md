# iTerm Alias Setup Instructions

This guide provides instructions on how to set up and use predefined aliases for iTerm that automate various development tasks.

## Overview

The aliases included are designed to streamline development operations such as syncing changes, starting servers, and deploying applications. They are part of a script that utilizes iTerm tabs to manage tasks efficiently.

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
