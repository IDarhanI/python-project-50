import argparse
import json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))


    diff = []

    for key in all_keys:
        if key not in data2:
            diff.append(f" - {key}: {format_value(data1[key])}")
        elif key not in data1:
            diff.append(f" + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            diff.append(f"    {key}: {format_value(data1[key])}")
        else:
            diff.append(f" - {key}: {format_value(data1[key])}")
            diff.append(f" + {key}: {format_value(data2[key])}")
    return "{\n" + "\n".join(diff) + "\n}"

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        prog='gendiff'
    )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    
    args = parser.parse_args()

    diff_generate = generate_diff(args.first_file, args.second_file)
    print(diff_generate)

if __name__ == "__main__":
    main()