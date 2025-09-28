# Python Project 50 - Gendiff

[![Actions Status](https://github.com/IDarhanI/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions)
[![CI](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)

Утилита для сравнения конфигурационных файлов и отображения различий между ними. Поддерживает JSON и YAML форматы с рекурсивным сравнением вложенных структур.

## 🎥 Демонстрация

### Сравнение JSON файлов
[![asciicast](https://asciinema.org/a/8MR7Wltk6XAQ05kBecxSxBKN4.svg)](https://asciinema.org/a/8MR7Wltk6XAQ05kBecxSxBKN4)

### Сравнение YAML файлов  
[![asciicast](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz.svg)](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz)

### Форматы вывода
[![asciicast](https://asciinema.org/a/TKc7yZcKR895c2oicRVU4an0Z.svg)](https://asciinema.org/a/TKc7yZcKR895c2oicRVU4an0Z)

## 📦 Установка

### Установка из репозитория
```bash
git clone https://github.com/IDarhanI/python-project-50.git
cd python-project-50
make install

Базовое использование
bash
gendiff file1.json file2.json
С поддержкой форматов вывода
bash
# Стандартный формат (stylish) - по умолчанию
gendiff file1.json file2.json

# Плоский формат
gendiff --format plain file1.json file2.json

# JSON формат
gendiff --format json file1.json file2.json
Поддерживаемые форматы файлов
JSON (.json)

YAML (.yml, .yaml)

🛠 Команды Makefile
Установка и сборка
bash
make install          # Установить зависимости
make build            # Собрать пакет
make package-install  # Установить пакет локально
Тестирование
bash
make test             # Запустить тесты
make test-coverage    # Запустить тесты с покрытием
make lint             # Проверить код линтером
make check            # Запустить тесты и проверку кода
Запуск утилиты
bash
make gendiff-json     # Сравнить JSON файлы
make gendiff-yaml     # Сравнить YAML файлы

