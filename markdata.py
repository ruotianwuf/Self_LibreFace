import time

import libreface
import json
import os
from concurrent.futures import ThreadPoolExecutor

reslist = []

# Directory containing subdirectories with images
base_image_directory = 'D:\\Genetic Programming\\LibreFace\\img_align_celeba'
output_directory = 'data'

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


def process_image(filename, output_subdirectory):
    if filename.endswith('.jpg'):
        image_path = os.path.join(base_image_directory, output_subdirectory, filename)
        json_output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_annotations.json")

        # Generate facial attributes and save to CSV
        res = libreface.get_facial_attributes(image_path, device='cuda:0')
        res['filename'] = filename
        # Save the dictionary to a JSON file
        with open(json_output_path, 'w') as json_file:
            json.dump(res, json_file, indent=4)
        # reslist.append(res)
        # print(f"{ filename } saved in list")



# Use ThreadPoolExecutor to manage a pool of threads
with ThreadPoolExecutor(max_workers=1) as executor:
    # Loop through all subdirectories in the base image directory
    for subdirectory in os.listdir(base_image_directory):
        if subdirectory == "1":  # 只处理名为"1"的子目录
            subdirectory_path = os.path.join(base_image_directory, subdirectory)
            if os.path.isdir(subdirectory_path):
                for filename in os.listdir(subdirectory_path):
                    executor.submit(process_image, filename, subdirectory)
            break  # 处理完第一个子目录后退出循环

print("All images have been processed.")