# Delete all CSV files in the output directory
import os


# Delete all PNG files in the image directory
for filename in os.listdir("img_align_celeba/1"):
    if filename.endswith('.png'):
        os.remove(os.path.join("img_align_celeba/1", filename))
        print(f"Deleted PNG file: {filename}")

for filename in os.listdir("data"):
    if filename.endswith('.json'):
        os.remove(os.path.join("data", filename))
        print(f"Deleted JSON file: {filename}")