import json
import yaml
from pathlib import Path

def parse_data(data, format_name):
    if format_name == 'json':
        return json.loads(data)
    elif format_name in ('yaml', 'yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError(f'Unsupported format: {format_name}')

def get_file_format(file_path):
    file_path_obj = Path(file_path)
    extension = file_path_obj.suffix.lower()

    if extension == '.json':
        return 'json'
    elif extension in ('.yaml', '.yml'):
        return 'yaml'
    else:
        raise ValueError(f'Unsupported file format: {extension}')

def load_file(file_path):
    format_name = get_file_format(file_path)

    with open(file_path, 'r') as file:
        content = file.read()
        return parse_data(content, format_name)