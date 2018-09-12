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

#### Run tests

```
$ nosetests -s tests
```

### Docker

##### Build image
```
$ docker-compose build
```

##### Create database

```
$ docker-compose run web python create_db.py
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
# Start database
$ docker-compose up -d db
```

```
# Create database for test
$ docker-compose run -e FLASK_ENV=test web python create_db.py
$ docker-compose run -e FLASK_ENV=test web python manage.py db upgrade
```

```
# Run test
$ docker-compose run -e FLASK_ENV=test web nosetests -s tests
```

