import os
import shutil
from pathlib import Path


# Define constants for file extensions
AUDIOS_EXT = ['.mp3', '.wav']
VIDEOS_EXT = ['.mp4', '.mov', '.avi']
IMAGES_EXT = ['.jpg', '.jpeg', '.png']
DOCUMENTS_EXT = ['.txt', '.pdf', 'docx']

def get_file_extension(file_name):
    """Returns the file extension of the given file name."""
    file_suffix = Path(file_name).suffix
    return file_suffix

def create_directory_if_not_exists(directory):
    """Creates a directory if it doesn't exist."""
    if not os.path.isdir(directory):
        os.mkdir(directory)

def organize(directory):
    """Organizes files into folders based on their extensions."""
    AUDIOS_DIR = os.path.join(directory, "audios")
    IMAGES_DIR = os.path.join(directory, "images")
    DOCS_DIR = os.path.join(directory, "documents")
    VIDEOS_DIR = os.path.join(directory, "videos")
    OTHERS_DIR = os.path.join(directory, "others")

    # Create directories if they don't exist
    create_directory_if_not_exists(AUDIOS_DIR)
    create_directory_if_not_exists(IMAGES_DIR)
    create_directory_if_not_exists(DOCS_DIR)
    create_directory_if_not_exists(VIDEOS_DIR)
    create_directory_if_not_exists(OTHERS_DIR)

    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(path, file))]

    for file_name in files:
        # Get the file extension in lowercase
        extension = get_file_extension(file_name).lower()

        if extension in AUDIOS_EXT:
            destination_dir = AUDIOS_DIR
        elif extension in VIDEOS_EXT:
            destination_dir = VIDEOS_DIR
        elif extension in IMAGES_EXT:
            destination_dir = IMAGES_DIR
        elif extension in DOCUMENTS_EXT:
            destination_dir = DOCS_DIR
        else:
            destination_dir = OTHERS_DIR

        # Move the file to the corresponding folder
        file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(destination_dir, file_name)
        shutil.move(file_path, new_file_path)

if __name__ == '__main__':
    path = input(r'Path: ')
    organize(path)