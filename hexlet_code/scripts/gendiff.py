import argparse
from .parsers import load_file
from .diff_builder import build_diff
from .formatters import format_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        raise ValueError(f'Unsupported format: {format_name}')


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        prog='gendiff'
    )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')
    
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()