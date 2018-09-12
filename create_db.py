import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from config import DevelopmentConfig, StagingConfig, ProductionConfig, TestConfig

env = os.environ.get('FLASK_ENV', 'development')
if env == 'development':
    config = DevelopmentConfig
elif env == 'staging':
    config = StagingConfig
elif env == 'production':
    config = ProductionConfig
elif env == 'test':
    config = TestConfig
else:
    raise Exception("No such environment is found: {}".format(env))

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))
