### Flask largeapp example

#### Structure

```
~/ExampleApp
    |-- manage.py
    |-- config.py
    |-- /app
        |-- __init__.py
        |-- /models
            |-- __init__.py
            |-- entry.py
            |-- user.py
        |-- /views
            |-- __init__.py
            |-- error.py
            |-- entry.py
            |-- user.py
        |-- /templates
            |-- layout.html
            |-- /entries
                |-- show_entries.html
            |-- /errors
                |-- 400.html
                |-- 404.html
                |-- 500.html
        |-- /static
            |-- style.css
    |-- /tests
        |-- __init__.py
        |-- /models
            |-- test_entry.py
        |-- /views
            |-- test_api.py

```

#### Install packages

```
$ pip install -r requirements.txt
```

#### Create Database (SQLite3)

Edit config.py and use SQLALCHEMY_DATABASE_URI which starts with "sqlite:///"
```
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///{path}/app.db".format(path=base_dir)  # Use this.
    ...
```

Then,
```
$ FLASK_ENV=development python manage.py db init
$ FLASK_ENV=development python manage.py db migrate
$ FLASK_ENV=development python manage.py db upgrade
```

You have to create database for test, too.
```
$ FLASK_ENV=test python manage.py db migrate
$ FLASK_ENV=test python manage.py db upgrade
```

#### Run server

```
$ FLASK_ENV=development python manage.py runserver
```

or

```
$ FLASK_ENV=development FLASK_APP=manage flask run
```

#### Run tests

Set PYTHONPATH, at first.
```
$ export PYTHONPATH=`pwd`
```

Then,
```
$ nosetests -s
```

### Docker

##### Build image
```
$ docker-compose build
```

##### Create database

```
$ docker-compose run web flask createdb
```

##### Create tables
```
$ docker-compose run web python manage.py db init
$ docker-compose run web python manage.py db migrate
$ docker-compose run web python manage.py db upgrade
```

##### Start web app
```
$ docker-compose up [-d]
```

##### Run tests

```
# Start database server
$ docker-compose up -d db
```

```
# Create database for test
$ docker-compose run -e FLASK_ENV=test web flask createdb
$ docker-compose run -e FLASK_ENV=test web python manage.py db upgrade
```

```
# Run test
$ docker-compose run -e FLASK_ENV=test web nosetests -s
```

##### Tips

```
# Connect postgresql database
$ docker exec -it flask-largeapp-sample_db_1 psql -U postgres flask_sampleapp_dev
```
