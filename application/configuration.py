class DefaultConfig(object):
    APP_NAME = 'flask-boilerplate'
    LOG_PATH = 'logs/application.log'
    ENV = 'INVALID'

class DevConfig(DefaultConfig):
    ENV = 'DEV'

class ProdConfig(DefaultConfig):
    ENV = 'PROD'
