import libreface
import pandas as pd
import json
import os

# Directory containing images
image_directory = 'img_align_celeba'
output_directory = 'data'

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through all images in the directory
for filename in os.listdir(image_directory):
    if filename.endswith('.jpg'):
        image_path = os.path.join(image_directory, filename)
        csv_output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_attributes.csv")
        json_output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_annotations.json")

        # Generate facial attributes and save to CSV
        libreface.get_facial_attributes(image_path, output_save_path=csv_output_path, device='cuda:0')

        # Load the CSV file with error handling
        try:
            data = pd.read_csv(csv_output_path)
        except Exception as e:
            print(f"Failed to load CSV file '{csv_output_path}': {e}")
            continue

        # Define a function to generate annotations from each row
        def generate_annotation(row):
            return {
                "facial_expression": row["facial_expression"],
                "head_pose": {
                    "pitch": row["pitch"],
                    "yaw": row["yaw"],
                    "roll": row["roll"]
                },
                "landmarks": {
                    key: row[key] for key in row.keys() if key.startswith("lm_mp_")
                },
                "action_units": {
                    key: row[key] for key in row.keys() if key.startswith("au_")
                }
            }

        # Generate annotations for each row
        annotations = [generate_annotation(row) for _, row in data.iterrows()]

        # Save annotations to a JSON file
        with open(json_output_path, 'w') as json_file:
            json.dump(annotations, json_file, indent=4)

        print(f"Annotation file has been generated and saved as '{json_output_path}'")

