import pytest
import os
from hexlet_code.scripts.gendiff import generate_diff


def get_fixture_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)


def read_fixture(filename):
    with open(get_fixture_path(filename), 'r') as f:
        return f.read()


@pytest.fixture
def expected_stylish():
    return read_fixture('expected_stylish.txt')


def test_stylish_format_json(expected_stylish):
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    result = generate_diff(file1, file2)
    assert result == expected_stylish


def test_stylish_format_yaml(expected_stylish):
    file1 = get_fixture_path('filepath1.yml')
    file2 = get_fixture_path('filepath2.yml')
    
    result = generate_diff(file1, file2)
    assert result == expected_stylish


def test_stylish_format_mixed_files():
    # Тест на одинаковые файлы
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file1.json')
    
    result = generate_diff(file1, file2)
    # Проверяем, что для одинаковых файлов вывод корректен
    assert 'common' in result
    assert 'group1' in result


def test_unsupported_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    with pytest.raises(ValueError, match="Unsupported format: unknown"):
        generate_diff(file1, file2, 'unknown')


def test_unsupported_file_format():
    # Создадим временный файл с неподдерживаемым расширением
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write('test content')
        temp_file = f.name
    
    file1 = get_fixture_path('file1.json')
    
    try:
        from hexlet_code.scripts.parsers import load_file
        with pytest.raises(ValueError, match="Unsupported file format"):
            load_file(temp_file)
    finally:
        os.unlink(temp_file)