
# Library CLI

Приложение командной стороки для выполнения операций добавления, удаления, получения, поиска данных из .json файла

## Требования к тестовому заданию

- Разработать консольное приложение для управления библиотекой книг
- Каждая книга должна содержать следующие поля:
  + id (уникальное значение, генерируется автоматически)
  + title
  + author
  + year
  + status (статус книги: "в наличии", "выдана")
- Режимы работы: добавление книги, удаление, поиск по title, author или year,  отображение всех книг, изменение статуса
- Реализовать хранение данных в текстовом или json формате
- Не использовать сторонние библиотеки

## Основные инструменты

- Python
- argparse -  cтандартная библиотека Python для создания интерфейсов командной строки -> [документация](https://docs.python.org/3/library/argparse.html)
- json - стандартная библиотека Python для работы с файлами формата .json -> [документация](https://docs.python.org/3/library/json.html)
- unittest - фреймворк для создания модульных тестов из стандартной библиотеки Python -> [документация](https://www.sqlite.org/)



## Установка

- Скопировать директорию с проектом на жесткий диск

- Используются стандартные библиотеки языка Python версии 3.10.12


    
## Доступный функционал и примеры использования

Точка входа - модуль library.py

Для просмотра доступных режимов работы

```bash
  python3 library.py -h
```

### Команды
- **create-json** создание файла db.json в директории проекта 

```bash
  python3 library create-json
  >>> json file is created
```

- **add** добавление новой книги командой add в формате: "TITLE" "AUTHOR" YEAR "STATUS"

```bash
  python3 library.py add "Капитанская дочка" "Пушкин" 1990 "в наличии"
  >>> book is added
```
Доступные варианты для команды STATUS - "в наличии" или "выдана"

- **list** вывод на экран всех книг

```bash
  python3 library.py list
  >>> {'id': 1, 'title': 'Капитанская дочка', 'author': 'Пушкин', 'year': '1990', 'status': 'в наличии'}
```

- **change** изменение статуса книги по id в формате: ID "выдана"

```bash
  python3 library.py change 1 "выдана"
  >>> {'id': 1, 'title': 'Капитанская дочка', 'author': 'Пушкин', 'year': '1990', 'status': 'выдана'}
  >>> status was changed
```

- **search** поиск в полях author, title, year по переданному значению в формате: QUERY

```bash
  python3 library.py search "Пушкин"
  >>> {'id': 1, 'title': 'Капитанская дочка', 'author': 'Пушкин', 'year': '1990', 'status': 'выдана'}
```

- **delete** удаление книги по id в формате: ID
```bash
  python3 library.py delete 1
  >>> book with id: 1 is deleted
```
## Тестирование

Тестирование реализовано в модуле tests.py, для запуска тестов:

```bash
  python3 -m unittest -v tests.py
```


## Отчет

Для создания интерфейса командной строки использована стандартная библиотека argparse. Библиотека автоматически создает команду вызова помощи -h и описания доступных команд проекта, также позволяет создавать парсеры для передачи аргументов переданных в командной строке функциям приложения.

В качестве базы данных использован файл формата .json. Не является оптимальным решением, при записи новых книг приходится перезаписывать файл целиком. Наиболее верным решением было бы использование базы данных, например SQLite, библиотека для работы с которой входит в стандартную библиотеку языка Python. 

Тестирование реализовано с помощью стандартной библиотеки unittest, которя позволяет проводит тестирования отдельных функций приложения. Используются методы setUp и tearDown класса unittest.TestCase для создания тестового json файла с предзаполненными тестовыми данными и удалением этого файла. Эти методы запускаются перед и после каждого теста.

Для автоматического форматирования кода использованы библиотеки [Black](https://github.com/psf/black) и [isort](https://pycqa.github.io/isort/).
