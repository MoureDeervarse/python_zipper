import os
import py7zr
from zippers.base import Zipper

class SevenZipper(Zipper):
    def compress(target_path, is_dir, output_file):
        with py7zr.SevenZipFile(output_file, 'w') as file:
            file.writeall(target_path, os.path.basename(target_path))

    def decompress(target_file, output_file):
        with py7zr.SevenZipFile(target_file, 'r') as file:
            file.extractall(path=output_file)

