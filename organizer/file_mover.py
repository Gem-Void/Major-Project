import os
import shutil
import time


def move_file(file_path, label):

    print("\n===================================")
    print("      FILE ORGANIZATION")
    print("===================================\n")

    base_folder = os.path.dirname(file_path)

    category_folder = os.path.join(base_folder, label)

    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    file_name = os.path.basename(file_path)

    new_path = os.path.join(category_folder, file_name)

    for i in range(3):

        try:

            shutil.move(file_path, new_path)

            print("File Moved Successfully")
            print("New Location :", new_path)

            return new_path

        except PermissionError:

            print(f"File locked. Retrying... ({i+1}/3)")

            time.sleep(1)

    raise Exception("Could not move file")