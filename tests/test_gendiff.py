import pytest
import json
import os
import re
from gendiff.scripts.gendiff import generate_diff


def get_fixture_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'test_data', filename)


def read_fixture(filename):
    with open(get_fixture_path(filename), 'r') as f:
        return f.read()


def normalize_whitespace(text):
    text = re.sub(r' +', ' ', text)
    text = re.sub(r' +\n', '\n', text)
    return text.strip()


@pytest.fixture
def expected_stylish():
    return read_fixture('expected_stylish.txt')


@pytest.fixture
def expected_plain():
    return read_fixture('expected_plain.txt')


def test_stylish_format_json(expected_stylish):
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    result = generate_diff(file1, file2)
    result_normalized = normalize_whitespace(result)
    expected_normalized = normalize_whitespace(expected_stylish)
    assert result_normalized == expected_normalized


def test_stylish_format_yaml(expected_stylish):
    file1 = get_fixture_path('filepath1.yml')
    file2 = get_fixture_path('filepath2.yml')
    
    result = generate_diff(file1, file2)
    result_normalized = normalize_whitespace(result)
    expected_normalized = normalize_whitespace(expected_stylish)
    assert result_normalized == expected_normalized


def test_plain_format_json(expected_plain):
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    result = generate_diff(file1, file2, 'plain')
    assert result == expected_plain


def test_plain_format_yaml(expected_plain):
    file1 = get_fixture_path('filepath1.yml')
    file2 = get_fixture_path('filepath2.yml')
    
    result = generate_diff(file1, file2, 'plain')
    assert result == expected_plain


def test_json_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    result = generate_diff(file1, file2, 'json')
    
    # Проверяем что результат валидный JSON
    parsed_result = json.loads(result)
    assert isinstance(parsed_result, list)
    
    # Проверяем структуру
    for item in parsed_result:
        assert 'key' in item
        assert 'type' in item
        assert item['type'] in ['added', 'removed', 'changed', 'unchanged', 'nested']


def test_json_format_yaml():
    file1 = get_fixture_path('filepath1.yml')
    file2 = get_fixture_path('filepath2.yml')
    
    result = generate_diff(file1, file2, 'json')
    
    # Проверяем что результат валидный JSON
    parsed_result = json.loads(result)
    assert isinstance(parsed_result, list)


def test_stylish_format_mixed_files():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file1.json')
    
    result = generate_diff(file1, file2)
    assert 'common' in result
    assert 'group1' in result


def test_unsupported_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    with pytest.raises(ValueError, match="Unsupported format: unknown"):
        generate_diff(file1, file2, 'unknown')