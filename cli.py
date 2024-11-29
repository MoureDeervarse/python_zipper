import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="File Compression and Decompression Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Compress command
    compress_parser = subparsers.add_parser('compress', help="Compress a file or directory")
    compress_parser.add_argument('target', help="Target file or directory path")
    compress_parser.add_argument('--format', choices=['zip', 'tar.gz', '7z'], default='zip', help="Compression format")

    # Decompress command
    decompress_parser = subparsers.add_parser('decompress', help="Decompress a file")
    decompress_parser.add_argument('target', help="Input compressed file path")
    
    return parser
