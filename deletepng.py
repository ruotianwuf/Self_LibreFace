# Delete all CSV files in the output directory
import os


for filename in os.listdir("data"):
    if filename.endswith('.csv'):
        os.remove(os.path.join("data", filename))
        print(f"Deleted CSV file: {filename}")

# Delete all PNG files in the image directory
for filename in os.listdir("img_align_celeba"):
    if filename.endswith('.png'):
        os.remove(os.path.join("img_align_celeba", filename))
        print(f"Deleted PNG file: {filename}")