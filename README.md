# Python Project 50 - Gendiff

[![Actions Status](https://github.com/IDarhanI/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions)
[![CI](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)

Утилита для сравнения конфигурационных файлов и отображения различий между ними.

## Демонстрация

[![asciicast](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz.svg)](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz)

## Сборка

**hexlet-check** - Статус автоматических проверок Hexlet.

## Качество кода (SonarQube)

- **Quality Gate Status: Passed** - Общий статус качества кода, определяемый SonarQube
- **Bugs** - Количество найденных багов
- **Code Smells** - Количество code smells (проблемных участков кода)
- **Duplicated Lines (%)** - Процент дублированного кода
- **Lines of Code** - Количество строк кода
- **Reliability Rating** - Рейтинг надежности кода
- **Security Rating** - Рейтинг безопасности кода
- **Technical Debt** - Оценка технического долга
- **Maintainability Rating** - Рейтинг поддерживаемости кода
- **Vulnerabilities** - Количество найденных уязвимостей
- **Coverage** - Покрытие кода тестами

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
4. Установите утилиту с помощью uv:
   ```bash
   uv sync --dev
   ```

## Использование

### Базовое использование
```bash
gendiff file1.json file2.json
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

## Разработка

### Установка для разработки
```bash
# Клонирование репозитория
git clone https://github.com/IDarhanI/python-project-50.git
cd python-project-50

# Установка зависимостей
uv sync --dev
```

### Запуск тестов
```bash
uv run pytest
```

### Проверка кодстайла
```bash
uv run ruff check .
uv run ruff format .
```

### Сборка пакета
```bash
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