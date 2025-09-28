# Python Project 50 - Gendiff

[![Actions Status](https://github.com/IDarhanI/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions)
[![CI](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/IDarhanI/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=IDarhanI_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=IDarhanI_python-project-50)

CLI утилита для сравнения конфигурационных файлов (JSON, YAML) с поддержкой рекурсивного сравнения вложенных структур.

## 🎥 Демонстрация

### Сравнение вложенных структур (Stylish)
[![asciicast](https://asciinema.org/a/8MR7Wltk6XAQ05kBecxSxBKN4.svg)](https://asciinema.org/a/8MR7Wltk6XAQ05kBecxSxBKN4)

### Сравнение JSON файлов (Plain)
[![asciicast](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz.svg)](https://asciinema.org/a/sqyC7z6Tzjn3ckX1NR3PmOrRz)

### Сравнение YAML файлов (Plain)
[![asciicast](https://asciinema.org/a/TKc7yZcKR895c2oicRVU4an0Z.svg)](https://asciinema.org/a/TKc7yZcKR895c2oicRVU4an0Z)

### Plain формат вывода
[![asciicast](https://asciinema.org/a/Rb7rqjufA2eTXH1pj5dLjGkry.svg)](https://asciinema.org/a/Rb7rqjufA2eTXH1pj5dLjGkry)

### JSON формат вывода
[![asciicast](https://asciinema.org/a/hUnN0RozzMrDr2IqMttR3YoUD)](https://asciinema.org/a/demo_json.cast)

## 📦 Установка
git clone https://github.com/IDarhanI/python-project-50.git
cd python-project-50
make install

🛠 Команды Makefile
Установка и сборка

make install          # Установить зависимости
make build            # Собрать пакет
make package-install  # Установить пакет локально
make force            # Принудительная переустановка пакета

Тестирование и проверка кода

make test             # Запустить тесты
make lint             # Проверить код линтером
make fix              # Автоисправление проблем кода
make check            # Запустить тесты и проверку кода

Запуск утилиты

make gendiff-json     # Сравнить JSON файлы (stylish)
make gendiff-yaml     # Сравнить YAML файлы (stylish)
make gendiff-plain    # Сравнить JSON файлы (plain)
make gendiff-plain-yaml # Сравнить YAML файлы (plain)
make gendiff-json-format # Сравнить JSON файлы (json)
make gendiff-json-format-yaml # Сравнить YAML файлы (json)
