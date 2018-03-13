class DefaultConfig(object):
    APP_NAME = 'flask-boilerplate'
    LOG_PATH = 'logs/application.log'
    ENVIRONMENT = 'INVALID'
    DEBUG = False
    HOST = '127.0.0.1'
    PORT = 5000

class DevConfig(DefaultConfig):
    ENVIRONMENT = 'DEV'
    DEBUG = True

class ProdConfig(DefaultConfig):
    ENVIRONMENT = 'PROD'
    PORT = 5050
