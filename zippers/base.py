from abc import *

class Zipper(metaclass=ABCMeta):
    @abstractmethod
    def compress(self, target_path, output_file):
        pass

    @abstractmethod
    def decompress(self, target_file, output_file):
        pass
