### Flask largeapp example

#### Structure

```
~/ExampleApp
    |-- manage.py
    |-- config.py
    |-- /app
        |-- __init__.py
        |-- models.py
        |-- /views
            |-- __init__.py
            |-- entry.py
        |-- /templates
            |-- layout.html
            |-- show_entries.html
        |-- /static
            |-- style.css
    |-- /tests
        |-- test_sample.py

```

#### Install packages

```
$ pip install -r requirements.txt
```

#### Create Database (SQLite3)

```
$ FLASK_ENV=development python manage.py db init
$ FLASK_ENV=development python manage.py db migrate
$ FLASK_ENV=development python manage.py db upgrade
```

Also, you have to create database for test.
```
$ FLASK_ENV=test python manage.py db migrate
$ FLASK_ENV=test python manage.py db upgrade
```

#### Run server

```
$ FLASK_ENV=development python manage.py runserver
```

#### Run tests

```
$ nosetests -s tests
```
