import os
from PIL import Image

def rename_and_compress_images(directory, max_size_kb=50):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            old_filepath = os.path.join(directory, filename)
            new_filename = filename.replace(' ', '-')
            new_filepath = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {old_filepath} -> {new_filepath}')

            # Check file size
            file_size_kb = os.path.getsize(new_filepath) / 1024  # Convert bytes to kilobytes
            if file_size_kb > max_size_kb:
                compress_image(new_filepath)
                print(f'Compressed: {new_filepath} (size: {file_size_kb:.2f} KB)')

def compress_image(filepath, quality=85):
    # Open an image file
    with Image.open(filepath) as img:
        # Compress the image and save it
        img.save(filepath, optimize=True, quality=quality)

# Specify the directory containing the images
image_directory = '/mnt/data/projects/expert-home/static/images/home'

# Call the function to rename and compress images
rename_and_compress_images(image_directory)
