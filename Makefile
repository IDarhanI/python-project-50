install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check

fix:
	uv run ruff check --fix

check: 
	test lint

build:
	uv build

force:
	uv tool install --force dist/*.whl

package-install:
	uv tool install dist/*.whl
	
gendiff-json:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json

gendiff-yaml:
	uv run gendiff tests/test_data/filepath1.yml tests/test_data/filepath2.yml

gendiff-plain:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json --format plain

gendiff-plain-yaml:
	uv run gendiff tests/test_data/filepath1.yml tests/test_data/filepath2.yml --format plain

gendiff-json-format:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json --format json

gendiff-json-format-yaml:
	uv run gendiff tests/test_data/filepath1.yml tests/test_data/filepath2.yml --format json
