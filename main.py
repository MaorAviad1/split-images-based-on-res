import os
from PIL import Image

# Define the directory
dir_path = 'images/'

# Loop over all files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # Open the image file
        with Image.open(os.path.join(dir_path, filename)) as img:
            # Get the width of the image
            width, _ = img.size

            # Define the new directory based on the width
            new_dir = os.path.join(dir_path, f'{width}px')

            # Create the new directory if it does not exist
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

            # Move the file to the new directory
            os.rename(os.path.join(dir_path, filename), os.path.join(new_dir, filename))
