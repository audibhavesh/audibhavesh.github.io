import os
import json

# Folder paths
input_folder = "images"
output_folder = "avatars"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Initialize the JSON list
image_list = []

# Process images
for index, filename in enumerate(sorted(os.listdir(input_folder)), start=1):
    # Parse the file details
    parts = filename.split(', ')
    if len(parts) != 2:
        continue

    girl_status = parts[0].split('=')[1].strip()
    avatar_number = parts[1].split('=')[1].strip().split('.')[0]

    # Determine boy or girl based on girl_status
    boy_or_girl = "girl" if girl_status == "On" else "boy"

    # New filename
    new_filename = f"avatar_{boy_or_girl}_{index:02}.jpg"
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, new_filename)

    # Rename and move the file
    os.rename(input_path, output_path)

    # Add entry to the JSON list
    image_entry = {
        "imageUrl": f"https://audibhavesh.github.io/{output_folder}/{new_filename}",
        "width": 256,
        "height": 256
    }
    image_list.append(image_entry)

# Write the JSON to a file
json_output_path = os.path.join("images.json")
with open(json_output_path, "w") as json_file:
    json.dump(image_list, json_file, indent=4)

print(f"Processed {len(image_list)} images and created images.json.")
