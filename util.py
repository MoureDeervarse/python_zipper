import os

def add_extension(file_path, new_extension):
    if not new_extension.startswith("."):
        new_extension = f".{new_extension}"
    base_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)
    file_without_ext = os.path.splitext(base_name)[0]
    return os.path.join(dir_name, file_without_ext + new_extension)

def remove_extension(file_path):
    base_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)
    file_without_ext = os.path.splitext(base_name)[0]
    return os.path.join(dir_name, file_without_ext)
