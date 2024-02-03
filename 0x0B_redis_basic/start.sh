#!/bin/bash

# Start Redis server
service redis-server start

# Check if the command argument is provided
if [ -z "$1" ]; then
    # If no command is provided, use `tail -f /dev/null` to keep the container running
    tail -f /dev/null
else
    # If a command is provided (e.g., when using `docker exec`), execute it
    exec "$@"
fi
