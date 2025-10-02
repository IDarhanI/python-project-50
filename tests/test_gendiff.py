import json
import os
import tempfile

import pytest

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain, format_value_plain
from gendiff.formatters.stylish import format_stylish, format_value
from gendiff.scripts.diff_builder import build_diff
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parsers import load_file, parse_data


def get_fixture_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, "test_data", filename)


def read_fixture(filename):
    with open(get_fixture_path(filename), "r") as f:
        return f.read()


def normalize_whitespace(text):
    lines = []
    for line in text.split("\n"):
        line = " ".join(line.split())
        lines.append(line)
    return "\n".join(lines).strip()


@pytest.fixture
def expected_stylish():
    return read_fixture("expected_stylish.txt")


@pytest.fixture
def expected_plain():
    return read_fixture("expected_plain.txt")


def test_stylish_format_json(expected_stylish):
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    result = generate_diff(file1, file2)
    result_normalized = normalize_whitespace(result)
    expected_normalized = normalize_whitespace(expected_stylish)
    assert result_normalized == expected_normalized


def test_stylish_format_yaml(expected_stylish):
    file1 = get_fixture_path("filepath1.yml")
    file2 = get_fixture_path("filepath2.yml")

    result = generate_diff(file1, file2)
    result_normalized = normalize_whitespace(result)
    expected_normalized = normalize_whitespace(expected_stylish)
    assert result_normalized == expected_normalized


def test_plain_format_json(expected_plain):
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    result = generate_diff(file1, file2, "plain")
    assert result == expected_plain


def test_plain_format_yaml(expected_plain):
    file1 = get_fixture_path("filepath1.yml")
    file2 = get_fixture_path("filepath2.yml")

    result = generate_diff(file1, file2, "plain")
    assert result == expected_plain


def test_json_format():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    result = generate_diff(file1, file2, "json")

    parsed_result = json.loads(result)
    assert isinstance(parsed_result, list)

    for item in parsed_result:
        assert "key" in item
        assert "type" in item
        assert item["type"] in [
            "added",
            "removed",
            "changed",
            "unchanged",
            "nested",
        ]


def test_json_format_yaml():
    file1 = get_fixture_path("filepath1.yml")
    file2 = get_fixture_path("filepath2.yml")

    result = generate_diff(file1, file2, "json")

    parsed_result = json.loads(result)
    assert isinstance(parsed_result, list)


def test_stylish_format_mixed_files():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file1.json")

    result = generate_diff(file1, file2)
    assert "common" in result
    assert "group1" in result


def test_unsupported_format():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    with pytest.raises(ValueError, match="Unsupported format: unknown"):
        generate_diff(file1, file2, "unknown")


def test_empty_files():
    """Тест для пустых файлов"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False
    ) as f1:
        json.dump({}, f1)
        temp_file1 = f1.name
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False
    ) as f2:
        json.dump({}, f2)
        temp_file2 = f2.name

    try:
        result = generate_diff(temp_file1, temp_file2)
        assert result == "{\n}"
    finally:
        os.unlink(temp_file1)
        os.unlink(temp_file2)


def test_simple_flat_structure():
    """Тест для простых плоских структур"""
    data1 = {"a": 1, "b": 2}
    data2 = {"a": 1, "b": 3, "c": 4}

    diff = build_diff(data1, data2)
    assert len(diff) == 3
    assert diff[0]["type"] == "unchanged"  # a: 1
    assert diff[1]["type"] == "changed"  # b: 2 -> 3
    assert diff[2]["type"] == "added"  # c: 4


def test_nested_structure():
    """Тест для вложенных структур"""
    data1 = {"a": {"b": 1}}
    data2 = {"a": {"b": 2, "c": 3}}

    diff = build_diff(data1, data2)
    assert diff[0]["type"] == "nested"
    assert "children" in diff[0]
    nested_diff = diff[0]["children"]
    assert len(nested_diff) == 2
    assert nested_diff[0]["type"] == "changed"  # b: 1 -> 2
    assert nested_diff[1]["type"] == "added"  # c: 3


def test_format_value_plain_edge_cases():
    """Тест для граничных случаев format_value_plain"""
    assert format_value_plain(None) == "null"
    assert format_value_plain(True) == "true"
    assert format_value_plain(False) == "false"
    assert format_value_plain("string") == "'string'"
    assert format_value_plain(123) == "123"
    assert format_value_plain(45.67) == "45.67"
    assert format_value_plain({"a": 1}) == "[complex value]"


def test_format_value_edge_cases():
    """Тест для граничных случаев format_value"""
    assert format_value(None, 0) == "null"
    assert format_value(True, 0) == "true"
    assert format_value(False, 0) == "false"
    assert format_value("string", 0) == "string"
    assert format_value(123, 0) == "123"
    assert format_value({}, 0) == "{}"
    assert format_value({"a": 1}, 0) == "{\n    a: 1\n}"


def test_parser_unsupported_format():
    """Тест для неподдерживаемого формата файла"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as f:
        f.write("some text")
        temp_file = f.name

    try:
        with pytest.raises(ValueError, match="Unsupported file format"):
            load_file(temp_file)
    finally:
        os.unlink(temp_file)


def test_parser_unsupported_data_format():
    """Тест для неподдерживаемого формата данных"""
    with pytest.raises(ValueError, match="Unsupported format"):
        parse_data("some data", "xml")


def test_file_not_found():
    """Тест для случая когда файл не найден"""
    with pytest.raises(FileNotFoundError):
        generate_diff("nonexistent1.json", "nonexistent2.json")


def test_build_diff_with_none_values():
    """Тест с None значениями"""
    data1 = {"a": None, "b": 1}
    data2 = {"a": None, "b": 2}

    diff = build_diff(data1, data2)
    assert diff[0]["type"] == "unchanged"  # a: None
    assert diff[1]["type"] == "changed"  # b: 1 -> 2


def test_plain_format_with_empty_diff():
    """Тест plain форматера с пустой разницей"""
    result = format_plain([])
    assert result == ""


def test_stylish_format_with_empty_diff():
    """Тест stylish форматера с пустой разницей"""
    result = format_stylish([])
    assert result == "{\n}"


def test_json_format_with_empty_diff():
    """Тест json форматера с пустой разницей"""
    result = format_json([])
    assert result == "[]"
