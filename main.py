from cli import get_parser

# from zippers.gz import LinuxZipper
# from zippers.sz import SevenZipper
# from zippers.zip import DefaultZipper

def main():
    parser = get_parser()
    args = parser.parse_args()

    # check format type supported or not
    if args.command == 'compress':
        pass
    elif args.command == 'decompress':
        # need to check duplicated name already exists
        pass
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
