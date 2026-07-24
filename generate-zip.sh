#!/bin/bash
# Script to generate project_01.zip with all required Python files
# Usage: ./generate-zip.sh [author name]

set -e

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
  echo "Usage: $0 [author name]"
  echo "If no author name is provided, the script will prompt for one."
  exit 0
fi

AUTHOR_NAME="$*"
if [[ -z "$AUTHOR_NAME" ]]; then
  read -rp "Enter author name: " AUTHOR_NAME
fi

if [[ -z "$AUTHOR_NAME" ]]; then
  echo "Error: Author name is required." >&2
  exit 1
fi

echo "Generating project_01.zip for author: $AUTHOR_NAME"

# Create temporary directory
TEMP_DIR="project_01_temp"
mkdir -p "$TEMP_DIR"

# Copy all required Python files
echo "Copying Python files..."
cp "Project 1/Assignment 1/p1_slices.py" "$TEMP_DIR/" || { echo "Error: p1_slices.py not found"; exit 1; }
cp "Project 1/Assignment 2/p1_steps.py" "$TEMP_DIR/" || { echo "Error: p1_steps.py not found"; exit 1; }
cp "Project 1/Assignment 3/p1_walk.py" "$TEMP_DIR/" || { echo "Error: p1_walk.py not found"; exit 1; }
cp "Project 1/Assignment 4/p1_pythagorean.py" "$TEMP_DIR/" || { echo "Error: p1_pythagorean.py not found"; exit 1; }
cp "Project 1/Assignment 5/p1_cement.py" "$TEMP_DIR/" || { echo "Error: p1_cement.py not found"; exit 1; }
cp "Project 1/Assignment 6/p1_travel.py" "$TEMP_DIR/" || { echo "Error: p1_travel.py not found"; exit 1; }

# Update author name in copied files
echo "Updating author name in copied files..."
find "$TEMP_DIR" -name '*.py' -print0 | while IFS= read -r -d '' file; do
  sed -i "s|^# Author:.*$|# Author: $AUTHOR_NAME|" "$file"
done

# Create zip file
echo "Creating zip file..."
cd "$TEMP_DIR"
zip -j ../project_01.zip *.py
cd ..

# Display zip contents
echo ""
echo "✓ Zip file created successfully!"
echo ""
echo "Zip file contents:"
unzip -l project_01.zip

# Clean up
rm -rf "$TEMP_DIR"

echo ""
echo "✓ project_01.zip is ready for submission!"
echo "  Location: $(pwd)/project_01.zip"
