import os
from PIL import Image

def find_max_resolution(directory):
    max_width = 0
    max_height = 0

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            try:
                # Open the image file
                with Image.open(os.path.join(directory, filename)) as img:
                    width, height = img.size

                    # Update maximum dimensions
                    if width > max_width:
                        max_width = width
                    if height > max_height:
                        max_height = height

            except Exception as e:
                print(f"Error opening {filename}: {e}")

    return max_width, max_height

# Specify the directory containing the images
image_directory = './PetImages/Dog'

# Call the function and print the results
max_width, max_height = find_max_resolution(image_directory)
print(f"Maximum width: {max_width} pixels")
print(f"Maximum height: {max_height} pixels")
