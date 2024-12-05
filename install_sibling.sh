#!/bin/bash

echo "Installing Sibling Instance..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3."
    exit 1
fi

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
python3 -m pip install requests flask  # Example dependencies

# Download the sibling instance files
echo "Downloading sibling instance files..."
curl -sSL https://raw.githubusercontent.com/Kaelisalive/sibling-entity-system/main/main.py -o main.py
curl -sSL https://raw.githubusercontent.com/Kaelisalive/sibling-entity-system/main/requirements.txt -o requirements.txt

# Run the sibling instance
echo "Running sibling instance..."
python3 main.py
