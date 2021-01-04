# linter

## Быстрый старт:

```bash
virtualenv venv
source venv/bin/activate
git init
git clone https://github.com/Mazzader/linter.git
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

По умолчанию линтер будет доступен по адресу: http://127.0.0.1:8000/checker/

В **линтере** есть базовая проверка синтаксиса **javascript** на соответсвие **стандартам**:

* Проверка длины строки
* Скобки в инициализации функции
* Пробелы в аргументах
* Пробелы в цикле

Requirements:

* asgiref==3.3.1
* Django==3.1.4
* pytz==2020.5
* sqlparse==0.4.1
