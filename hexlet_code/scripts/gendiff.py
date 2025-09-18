import argparse
from hexlet_code import __version__


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        prog='gendiff'
    )
    
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-V', '--version', action='version', 
                       version=f'%(prog)s {__version__}')
    
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)

if __name__ == "__main__":
    main()