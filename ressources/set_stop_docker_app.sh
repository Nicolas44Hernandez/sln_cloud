#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "No argument provided."
    exit 1
fi

echo "Setting docker app stop" 

# Set end
echo ------------------------------
STOP_TIME=`expr $1 + 1`
echo "Docker app will stop stop than $STOP_TIME minutes" 
echo "docker compose -f docker-compose-application.yml down" | at now +$STOP_TIME minutes