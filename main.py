import os

from cli import get_parser, get_zipper_by_format, get_zipper_by_name
from util import add_extension, remove_extension
# from zippers.gz import LinuxZipper
# from zippers.sz import SevenZipper
# from zippers.zip import DefaultZipper

def main():
    parser = get_parser()
    args = parser.parse_args()

    if not os.path.exists(args.target):
        print(f"Target file [{args.target}] doesn't exists.")
        return
    
    if args.command == 'compress':
        zipper = get_zipper_by_format(args.format)
        if zipper == None:
            print(f"Format type [{args.format}] is not supported")
            return
        
        if args.output == '':
            args.output = add_extension(args.target, args.format)

        zipper.compress(args.target, args.output)
        print("Compress successed")

    elif args.command == 'decompress':
        # @TODO need to check duplicated name already exists
        zipper = get_zipper_by_name(args.target)
        if zipper == None:
            print(f"Format type [{args.target}] is not supported")
            return
        
        if args.output == '':
            args.output = remove_extension(args.target)

        zipper.decompress(args.target, args.output)
        print("Decompress successed")

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
