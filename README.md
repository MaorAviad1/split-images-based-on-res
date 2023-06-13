Here is a sample README file for your Python script:

# Image Sorting Script

## Description
This script is designed to sort images from a single directory into sub-directories based on the width of the image. For instance, an image with a width of 1600 pixels will be moved to a sub-directory named '1600px'.

## Usage
1. Ensure you have Python installed on your system. This script has been tested with Python 3.8, but should work with other versions as well.
2. Install the necessary Python packages by running the following command in your terminal:
    ```
    pip install pillow
    ```
3. Download the script `image_sorter.py` and place it in the parent directory of your images.
4. Modify the `dir_path` in the script to point to the directory of images you want to sort.
5. Run the script by navigating to the script's directory in your terminal and running the following command:
    ```
    python image_sorter.py
    ```
6. The script will create new sub-folders in the `dir_path` directory and move images into the appropriate folders.

## Requirements
- Python 3+
- Pillow library (`pip install pillow`)

## Note
The script supports '.png', '.jpg', and '.jpeg' file types. Additional file types may be added by modifying the `if` statement in the script.

Please ensure you have the necessary permissions for file and directory operations in the specified path. Also, it's recommended to back up your data before running the script to prevent accidental data loss.

## Disclaimer
This script is provided "as is", without warranty of any kind, express or implied. Use it at your own risk. Always make a backup of your data before using scripts that modify file systems.
