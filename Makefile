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
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

gendiff-yaml:
	uv run gendiff tests/fixtures/filepath1.yml tests/fixtures/filepath2.yml