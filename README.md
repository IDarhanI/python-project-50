# Python Project 50 - Gendiff

[![Actions Status](https://github.com/IDarhanI/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions)
[![CI](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)

Утилита для сравнения конфигурационных файлов и отображения различий между ними.

## Демонстрация

[![asciicast](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz.svg)](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz)


## Установка

1. Убедитесь, что в вашей системе установлен Python 3.12 или выше
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/IDarhanI/python-project-50.git
   ```
3. Перейдите в директорию проекта:
   ```bash
   cd python-project-50
   ```
4. Установите зависимости с помощью uv:
   ```bash
   make install
   ```

## Использование

### Базовое использование
```bash
gendiff file1.json file2.json
```

### Через Makefile
```bash
make gendiff
```

### Форматы вывода
Утилита поддерживает различные форматы вывода различий:
```bash
# Стандартный формат (stylish)
gendiff file1.json file2.json

# Плоский формат
gendiff --format plain file1.json file2.json

# JSON формат
gendiff --format json file1.json file2.json
```

### Поддерживаемые форматы файлов
- JSON (.json)
- YAML (.yml, .yaml)

## Примеры

### Сравнение JSON файлов
```bash
gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```

### Сравнение YAML файлов
```bash
gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
```

## Команды Makefile

### Установка и сборка
```bash
make install      # Установить зависимости
make build        # Собрать пакет
make package-install # Установить пакет локально
make force        # Принудительная переустановка пакета
```

### Тестирование и проверка кода
```bash
make test         # Запустить тесты
make test-coverage # Запустить тесты с покрытием
make lint         # Проверить код стилем
make check        # Запустить тесты и проверку кода
```

### Запуск утилиты
```bash
make gendiff      # Запустить сравнение тестовых файлов
make run          # Запустить пакет (если применимо)
```

## Разработка

### Установка для разработки
```bash
# Клонирование репозитория
git clone https://github.com/IDarhanI/python-project-50.git
cd python-project-50

# Установка зависимостей
make install
```

### Стандартный workflow разработки
```bash
# Установить зависимости
make install

# Запустить тесты и проверку кода
make check

# Собрать пакет
make build

# Протестировать установку
make package-install

# Проверить работу утилиты
make gendiff
```

### Ручной запуск команд (альтернатива Makefile)
```bash
# Установка зависимостей
uv sync --dev

# Запуск тестов
uv run pytest

# Проверка кодстайла
uv run ruff check .

# Сборка пакета
uv build
```

## Структура проекта
```
python-project-50/
├── hexlet_code/          # Исходный код утилиты
│   └── scripts/
│       └── gendiff.py    # Основной модуль
├── tests/               # Тесты
│   └── fixtures/        # Тестовые файлы
├── Makefile            # Команды для разработки
└── pyproject.toml      # Конфигурация проекта
```

## Системные требования
- Python 3.12 или выше
- uv