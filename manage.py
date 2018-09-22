import os
from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager, Server

config = {
    'development': 'config.DevelopmentConfig',
    'staging': 'config.StagingConfig',
    'production': 'config.ProductionConfig',
    'test': 'config.TestConfig',
}

env = os.environ.get('FLASK_ENV', 'development')
app = create_app(config[env])

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=os.environ.get('FLASK_RUN_PORT', 5000)))


@app.cli.command('createdb')
def create_db():
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
    print(database_exists(engine.url))


if __name__ == "__main__":
    manager.run()
