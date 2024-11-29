import os
import tarfile
from zippers.base import Zipper

class LinuxZipper(Zipper):
    def compress(target_path, is_dir, output_file):
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(target_path, arcname=os.path.basename(target_path))

    def decompress(target_file, output_file):
        with tarfile.open(target_file, "r:gz") as tar:
            tar.extractall(path=output_file)
