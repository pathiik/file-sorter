# File Sorter
This script sorts files in a directory based on their extensions. It moves a file into a subfolder with the same name as the file extension.

## How It Works
1. Prompts the user to enter the path of the directory they want to sort.
2. For each file in the directory:
   - Reads the filename of each file and extracts its extension.
   - Creates a subfolder named `<extension> Files` if it doesn't exist.
   - Moves the file into the subfolder.
3. If the file does not have an extension or is a directory, it displays the message `<file> does not have an extension`.

### Example:
1. Existing files:
    - test.py
    - test.txt
    - test.md
2. Reads the filename and creates a folder for each extension:
    - test.py -> py Files `<test.py> moved to <py Files>`
    - test.txt -> txt Files `<test.txt> moved to <txt Files>`
    - test.md -> md Files `<test.md> moved to <md Files>`
3. Moves the files into its respective folder:
    - py Files:
        - test.py
    - txt Files:
        - test.py
    - md Files:
        - test.md

## Duplicate Files
Files that already exist inside a subfolder will be considered duplicate files and will be moved to a separate subfolder named `Duplicate Files`.

#### How It Works
1. If a file with the same filename exists inside any subfolder named `<extension> Files`:
    - Creates a subfolder named `Duplicate Files`.
    - Moves the duplicate file to the folder.
    - Displays a message `<file> already exists in <extension> Files folder and has been moved to Duplicate Files folder`.

2. If a file exists in both `<extension> Files` and `Duplicate Files` folder:
    - Displays a message `<file> already exists in <extension> Files and Duplicate Files folders`.

## Run Locally
Clone the project
```bash
git clone https://github.com/pathiik/file-sorter.git
```
### Prerequisites
- `Python 3.11.9`

### Support
If you like this project, give it a ⭐ and share it with friends!

### Feedback
If you have any feedback or queries, please reach out to me at pathik.b45@gmail.com

###### Pathik Bhattarai