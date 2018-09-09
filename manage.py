import os
from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager, Server

env = os.environ.get('FLASK_ENV', 'development')
if env == 'development':
    config_file = 'config.DevelopmentConfig'
elif env == 'staging':
    config_file = 'config.StagingConfig'
elif env == 'production':
    config_file = 'config.ProductionConfig'
elif env == 'test':
    config_file = 'config.TestConfig'
else:
    raise Exception("No such environment is found: {}".format(env))

app = create_app(config_file)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000)))

if __name__ == "__main__":
    manager.run()
