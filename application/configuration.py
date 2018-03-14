import os

class DefaultConfig(object):
    APP_NAME = 'flask-boilerplate'
    LOG_PATH = 'logs/application.log'
    ENVIRONMENT = 'DEFAULT'
    DEBUG = False
    FLASK_HOST = '127.0.0.1'
    FLASK_PORT = 5000

class Config(DefaultConfig):
    FLASK_PORT = os.getenv('FLASK_PORT', 5000)
