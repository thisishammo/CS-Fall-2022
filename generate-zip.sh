#!/bin/bash
# Script to generate project_01.zip with all required Python files

set -e

echo "Generating project_01.zip..."

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
