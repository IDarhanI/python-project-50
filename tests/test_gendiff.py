import os
import pytest
from hexlet_code.scripts.gendiff import generate_diff
from hexlet_code.scripts.parsers import get_file_format, parse_data, load_file


def get_fixture_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()


def test_generate_diff_json():
    file1_path = get_fixture_path('file1.json')
    file2_path = get_fixture_path('file2.json')
    expected_path = get_fixture_path('expected_result.txt')
    
    result = generate_diff(file1_path, file2_path)
    expected = read_file(expected_path)
    
    assert result == expected


def test_generate_diff_yaml():
    # Используем существующие файлы с расширением .yml
    file1_path = get_fixture_path('filepath1.yaml')
    file2_path = get_fixture_path('filepath2.yaml')
    expected_path = get_fixture_path('expected_result.txt')
    
    result = generate_diff(file1_path, file2_path)
    expected = read_file(expected_path)
    
    assert result == expected


def test_generate_diff_same_files():
    file1_path = get_fixture_path('file1.json')
    result = generate_diff(file1_path, file1_path)
    
    # Проверяем, что все строки показывают одинаковые значения
    lines = result.split('\n')
    for line in lines[1:-1]:  # Пропускаем фигурные скобки
        if line.strip():  # Пропускаем пустые строки
            assert line.startswith('   ')


def test_get_file_format():
    assert get_file_format('file.json') == 'json'
    assert get_file_format('file.yaml') == 'yaml'
    assert get_file_format('file.yml') == 'yaml'
    
    with pytest.raises(ValueError):
        get_file_format('file.txt')


def test_parse_data():
    # Тест JSON
    json_data = '{"key": "value", "number": 123}'
    result = parse_data(json_data, 'json')
    assert result == {"key": "value", "number": 123}
    
    # Тест YAML
    yaml_data = 'key: value\nnumber: 123\nboolean: true'
    result = parse_data(yaml_data, 'yaml')
    assert result == {"key": "value", "number": 123, "boolean": True}
    
    # Тест неподдерживаемого формата
    with pytest.raises(ValueError):
        parse_data('some data', 'xml')


def test_load_file():
    # Тест загрузки JSON файла
    json_path = get_fixture_path('file1.json')
    result = load_file(json_path)
    expected = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    assert result == expected


def test_generate_diff_format():
    from hexlet_code.scripts.gendiff import format_value
    
    assert format_value(True) == "true"
    assert format_value(False) == "false"
    assert format_value(None) == "null"
    assert format_value("test") == "test"
    assert format_value(123) == "123"