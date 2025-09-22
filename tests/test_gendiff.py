import os
from hexlet_code.scripts.gendiff import generate_diff

def get_fixture_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def test_generate_diff_plain_json():
    file1_path = get_fixture_path('file1.json')
    file2_path = get_fixture_path('file2.json')
    expected_path = get_fixture_path('expected_result.txt')
    
    result = generate_diff(file1_path, file2_path)
    expected = read_file(expected_path)
    
    assert result == expected

def test_generate_diff_same_files():
    file1_path = get_fixture_path('file1.json')
    result = generate_diff(file1_path, file1_path)
    
    
    lines = result.split('\n')
    for line in lines[1:-1]:
        assert line.startswith('   ')

def test_generate_diff_format():
    from hexlet_code.scripts.gendiff import format_value
    
    assert format_value(True) == "true"
    assert format_value(False) == "false"
    assert format_value(None) == "null"
    assert format_value("test") == "test"
    assert format_value(123) == "123"