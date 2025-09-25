import os
import pytest
from hexlet_code.scripts.gendiff import generate_diff
from hexlet_code.scripts.parsers import get_file_format, parse_data, load_file
from hexlet_code.scripts.diff_builder import build_diff


def get_fixture_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()


def test_generate_diff_stylish_json():
    file1_path = get_fixture_path('file1.json')
    file2_path = get_fixture_path('file2.json')
    expected_path = get_fixture_path('expected_stylish.txt')
    
    result = generate_diff(file1_path, file2_path, 'stylish')
    expected = read_file(expected_path)
    
    assert result == expected


def test_generate_diff_stylish_yaml():
    file1_path = get_fixture_path('file1.yaml')
    file2_path = get_fixture_path('file2.yaml')
    expected_path = get_fixture_path('expected_stylish.txt')
    
    result = generate_diff(file1_path, file2_path, 'stylish')
    expected = read_file(expected_path)
    
    assert result == expected


def test_build_diff():
    data1 = {'key': 'value'}
    data2 = {'key': 'value', 'new_key': 'new_value'}
    
    diff = build_diff(data1, data2)
    
    assert len(diff) == 2
    assert diff[0] == {'key': 'key', 'type': 'unchanged', 'value': 'value'}
    assert diff[1] == {'key': 'new_key', 'type': 'added', 'value': 'new_value'}


def test_build_diff_nested():
    data1 = {'nested': {'key': 'value'}}
    data2 = {'nested': {'key': 'changed'}}
    
    diff = build_diff(data1, data2)
    
    assert diff[0]['type'] == 'nested'
    assert diff[0]['children'][0]['type'] == 'changed'