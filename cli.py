import argparse

from zippers.gz import LinuxZipper
from zippers.sz import SevenZipper
from zippers.zip import DefaultZipper
# from zippers.base import Zipper

support_formats = ('zip', 'tar.gz', '7z')

def get_zipper_by_format(target_format):
    if target_format == 'zip':
        return DefaultZipper()
    elif target_format == 'tar.gz':
        return LinuxZipper()
    elif target_format == '7z':
        return SevenZipper()
    else:
        return None
    
def get_zipper_by_name(file_name: str):
    if file_name.endswith('.zip'):
        return DefaultZipper()
    elif file_name.endswith('.7z'):
        return SevenZipper()
    elif file_name.endswith('.tar.gz'):
        return LinuxZipper()
    else:
        return None

def get_parser():
    parser = argparse.ArgumentParser(description="File Compression and Decompression Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Compress command
    compress_parser = subparsers.add_parser('compress', help="Compress a file or directory")
    compress_parser.add_argument('target', help="Target file or directory path")
    compress_parser.add_argument('--output', default='', help="Output file name. use same name fo target if you don't provide")
    compress_parser.add_argument('--format', choices=support_formats, default='zip', help="Compression format")

    # Decompress command
    decompress_parser = subparsers.add_parser('decompress', help="Decompress a file")
    decompress_parser.add_argument('target', help="Input compressed file path")
    decompress_parser.add_argument('--output', default='', help="Output file name. use same name fo target if you don't provide")
    
    return parser
