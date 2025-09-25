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

gendiff-flat-json:
	gendiff tests/fixtures/file1.json tests/fixtures/file2.json

gendiff-flat-yaml:
	gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml

gendiff-nested-json:
	gendiff tests/fixtures/file1_nested.json tests/fixtures/file2_nested.json

gendiff-nested-yaml:
	gendiff tests/fixtures/file1_nested.yaml tests/fixtures/file2_nested.yaml