#!/bin/bash

# Start Container and Echo Message to Console
echo "MySQL_Advanced Docker container started successfully ..."

# Check if the command argument is provided
if [ -z "$1" ]; then
    # If no command is provided, use `tail -f /dev/null` to keep the container running
    tail -f /dev/null
else
    # If a command is provided (e.g., when using `docker exec`, 'exec-cmd'), execute it
    exec "$@"
fi
