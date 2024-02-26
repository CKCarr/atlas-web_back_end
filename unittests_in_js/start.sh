#!/bin/bash

DIR=unittests_in_js

# Automatically change to the desired directory
echo "cd /$DIR" >> ~/.bashrc
echo "force_color_prompt=yes" >> ~/.bashrc
# Apply changes without needing to re-login
source ~/.bashrc

# Check if the command argument is provided
if [ -z "$1" ]; then
    # If no command is provided, use `tail -f /dev/null` to keep the container running
    tail -f /dev/null
else
    # If a command is provided (e.g., when using `docker exec`, 'exec-cmd'), execute it
    exec "$@"
fi
