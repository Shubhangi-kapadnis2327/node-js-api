import zipfile
import os

# Define file path
zip_file_path = "/mnt/data/node-js-api-main.zip"
extract_folder = "/mnt/data/node-js-api-main"

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# List extracted files
extracted_files = []
for root, dirs, files in os.walk(extract_folder):
    for file in files:
        extracted_files.append(os.path.join(root, file))

# Show a list of extracted files
extracted_files[:10]  # Show only first 10 files for preview
