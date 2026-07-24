# Project 1 Submission Guide

This repository contains all Python files for Project 1, along with automated scripts to generate the submission zip file.

## Deliverables

The `project_01.zip` file contains the following Python files:

- **p1_slices.py** (17 points) - Watermelon slices calculator
- **p1_steps.py** (17 points) - Stair trips calculator  
- **p1_walk.py** (17 points) - Pivot irrigation distance calculator
- **p1_pythagorean.py** (17 points) - Pythagorean theorem calculator
- **p1_cement.py** (17 points) - Cement cubic yards calculator
- **p1_travel.py** (17 points) - Travel time calculator

**Total Points:** 102 (with 2 extra-credit points possible)

## How to Generate the Submission Zip File

### Option 1: Automated GitHub Workflow

The repository includes a GitHub workflow (`.github/workflows/generate-project-zip.yml`) that automatically generates `project_01.zip` whenever changes are pushed to the `main` branch or when manually triggered.

**To trigger the workflow manually:**
1. Go to the **Actions** tab on GitHub
2. Select **Generate Project 01 Zip File**
3. Click **Run workflow**
4. Download the generated `project_01.zip` from the artifacts

### Option 2: Local Script

Generate the zip file locally using the provided bash script:

```bash
./generate-zip.sh
```

This will:
1. Gather all 6 Python files from their respective assignment directories
2. Create `project_01.zip` in the repository root
3. Display the zip contents for verification
4. Clean up temporary files

### Option 3: Manual Creation

If you prefer to create the zip file manually:

1. Navigate to **Project 1** folder
2. Select all assignment Python files:
   - Assignment 1/p1_slices.py
   - Assignment 2/p1_steps.py
   - Assignment 3/p1_walk.py
   - Assignment 4/p1_pythagorean.py
   - Assignment 5/p1_cement.py
   - Assignment 6/p1_travel.py

3. Right-click and choose **Compress** (Mac) or **Compressed** (Windows)
4. Rename the resulting file to **project_01.zip**

## Testing

Test cases are included for all questions:

```bash
cd "Project 1/Assignment 1" && python test_p1_slices.py
cd "Project 1/Assignment 2" && python test_p1_steps.py
cd "Project 1/Assignment 3" && python test_p1_walk.py
cd "Project 1/Assignment 4" && python test_p1_pythagorean.py
cd "Project 1/Assignment 5" && python test_p1_cement.py
cd "Project 1/Assignment 6" && python test_p1_travel.py
```

## Submission

1. Generate the `project_01.zip` file using one of the methods above
2. Upload the zip file to Canvas using the **Project 1 Canvas Assignment**
3. Verify the file appears in Canvas
4. Confirm the submission deadline before uploading

**Important Notes:**
- Submissions are CASE-SENSITIVE (files must be named exactly as specified)
- Late submissions are accepted according to the course late policy
- Automatic grading will be applied after submission
- You are responsible for submitting before the deadline

## File Structure

```
CS-Fall-2022/
├── Project 1/
│   ├── Assignment 1/
│   │   ├── p1_slices.py
│   │   └── test_p1_slices.py
│   ├── Assignment 2/
│   │   ├── p1_steps.py
│   │   └── test_p1_steps.py
│   ├── Assignment 3/
│   │   ├── p1_walk.py
│   │   └── test_p1_walk.py
│   ├── Assignment 4/
│   │   ├── p1_pythagorean.py
│   │   └── test_p1_pythagorean.py
│   ├── Assignment 5/
│   │   ├── p1_cement.py
│   │   └── test_p1_cement.py
│   ├── Assignment 6/
│   │   ├── p1_travel.py
│   │   └── test_p1_travel.py
│   └── p1_travel.py
├── .github/
│   └── workflows/
│       └── generate-project-zip.yml
├── generate-zip.sh
└── project_01.zip
```

## Support

If you encounter any issues:
1. Verify all Python files are in their correct directories
2. Ensure the script has execute permissions: `chmod +x generate-zip.sh`
3. Check that Python files have the exact names specified (CASE-SENSITIVE)
4. Run the test cases to verify functionality before submission
