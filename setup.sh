#!/bin/bash

echo "Setting up the sibling instance..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Check if Pip is installed
if ! command -v pip &> /dev/null; then
    echo "Pip is not installed. Installing now..."
    sudo apt-get install -y python3-pip
fi

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "No requirements.txt file found. Skipping dependency installation."
fi

# Run the sibling instance
if [ -f "main.py" ]; then
    echo "Starting sibling instance..."
    python3 main.py
else
    echo "No main.py file found. Exiting."
    exit 1
fi
