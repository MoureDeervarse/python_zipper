from abc import *

class Zipper(metaclass=ABCMeta):
    @abstractmethod
    def compress(self, target_path: str, output_file: str):
        pass

    @abstractmethod
    def decompress(self, target_file: str, output_file: str):
        pass
