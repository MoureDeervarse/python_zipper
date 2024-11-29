import os
import zipfile

from zippers.base import Zipper

class DefaultZipper(Zipper):
    def compress(self, target_path: str, output_file: str):
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isdir(target_path):
                for root, dirs, files in os.walk(target_path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, target_path)
                        zipf.write(full_path, arcname)
            else:
                zipf.write(target_path, os.path.basename(target_path))

    def decompress(self, target_file: str, output_file: str):
        with zipfile.ZipFile(target_file, 'r') as zipf:
            zipf.extractall(output_file)

