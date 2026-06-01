import os

def rename_file(file_path, new_name):

    folder = os.path.dirname(file_path)
    ext = os.path.splitext(file_path)[1]

    new_path = os.path.join(folder, new_name + ext)

    counter = 1

    while os.path.exists(new_path):

        new_path = os.path.join(
            folder,
            f"{new_name}_{counter}{ext}"
        )

        counter += 1

    os.rename(file_path, new_path)

    return new_path