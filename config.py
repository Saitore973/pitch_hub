import os

class config:
    SECRET_KEY =SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'

class ProdConfig(config):
    pass

class DevConfig(config):
    pass

config_options={
    'development': DevConfig,
    'production': ProdConfig
}