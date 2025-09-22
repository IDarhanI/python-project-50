install:
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

lint:
	uv run ruff check

check: 
	test lint

build:
	uv build

force:
	uv tool install --force dist/*.whl

package-install:
	uv tool install dist/*.whl
gendiff:
	gendiff tests/fixtures/file1.json tests/fixtures/file2.json