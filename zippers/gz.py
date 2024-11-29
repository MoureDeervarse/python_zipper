import os
import tarfile
from zippers.base import Zipper

class LinuxZipper(Zipper):
    def compress(self, target_path: str, output_file: str):
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(target_path, arcname=os.path.basename(target_path))

    def decompress(self, target_file: str, output_file: str):
        with tarfile.open(target_file, "r:gz") as tar:
            tar.extractall(path=output_file)
