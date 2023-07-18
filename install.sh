#!/bin/bash

# Check for Node.js
if command -v node &> /dev/null; then
  echo "Node.js is already installed!"
else
  echo "Node.js is not installed. Please install it."
  echo "Visit https://nodejs.org/ to download and install Node.js."
  echo "After installation, please run this script again."
  read -p "Press Enter to continue..."
fi

# Check for Python
if command -v python &> /dev/null; then
  echo "Python is already installed!"
else
  echo "Python is not installed. Please install it."
  echo "Visit https://www.python.org/downloads/ to download and install Python."
  echo "After installation, please run this script again."
  read -p "Press Enter to continue..."
fi

echo "Check complete!"

echo "Create virtual environment"
python3 -m venv venv
source venv/bin/activate
venv/bin/python -m pip install -r requirements.txt

echo "Initialize Vue environment"
npm install --save
cd web
npm install --save
npm run build
