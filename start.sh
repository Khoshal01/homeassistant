#!/bin/bash

echo "Starting Inverter Control Add-on..."

# Ensure shared directory exists
if [ ! -d "/share/inverter_control" ]; then
  mkdir -p /share/inverter_control
  chmod -R 777 /share/inverter_control
fi

# Run the main script
python3 /usr/src/app/test_inverter.py
