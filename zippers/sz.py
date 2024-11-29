import os
import py7zr
from zippers.base import Zipper

class SevenZipper(Zipper):
    def compress(self, target_path: str, output_file: str):
        with py7zr.SevenZipFile(output_file, 'w') as file:
            file.writeall(target_path, os.path.basename(target_path))

    def decompress(self, target_file: str, output_file: str):
        with py7zr.SevenZipFile(target_file, 'r') as file:
            file.extractall(path=output_file)

