import os
import shutil


def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Archives": [".zip", ".tar.gz"],
    }

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for folder, extensions in file_types.items():
                if ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)
                    print(f"Moved {file} to {folder}.")
                    break


# Example Usage
directory_to_organize = input("Enter the directory path to organize: ")
organize_files(directory_to_organize)
