from abc import *

class Zipper(metaclass=ABCMeta):
    @abstractmethod
    def compress(target_path, output_file):
        pass

    @abstractmethod
    def decompress(target_file, output_file):
        pass
