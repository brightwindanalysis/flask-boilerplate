import logging
from logging.handlers import TimedRotatingFileHandler

class Logger(object):
    
    def __init__(self, path_logs):
        self.path_logs = path_logs     
    
    def init(self, app):
        formatter = logging.Formatter("[%(asctime)s] [%(pathname)s:%(lineno)d] %(levelname)s - %(message)s")
        handler = TimedRotatingFileHandler(self.path_logs, when='midnight', interval=1, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.DEBUG)
