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

app = create_app(config[os.environ.get('FLASK_ENV', 'development')])

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=os.environ.get('FLASK_RUN_PORT', 5000)))

if __name__ == "__main__":
    manager.run()
