import os
import shutil
import time

# Constants for source and destination directories
SOURCE_DIRECTORY = "z:/path/to/seestar/folder"
DESTINATION_DIRECTORY = "C:/path/to/local/folder"

# Ensure destination directory exists
if not os.path.exists(DESTINATION_DIRECTORY):
    os.makedirs(DESTINATION_DIRECTORY)

def copy_fit_files():
    # Get list of .fit files in the source directory
    source_files = [f for f in os.listdir(SOURCE_DIRECTORY) if f.endswith('.fit')]
    
    for file_name in source_files:
        source_file_path = os.path.join(SOURCE_DIRECTORY, file_name)
        destination_file_path = os.path.join(DESTINATION_DIRECTORY, file_name)

        # Copy file if it doesn't exist in the destination
        if not os.path.exists(destination_file_path):
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied: {file_name}")

def main():
    while True:
        copy_fit_files()
        # Wait for 1 minute (60 seconds)
        time.sleep(60)

if __name__ == "__main__":
    main()
