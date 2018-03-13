import os
import logging
from logging.handlers import TimedRotatingFileHandler

class Logger(object):
    
    def __init__(self, path_logs):
        self.path_logs = path_logs     
    
    def init(self, app):
        os.makedirs(os.path.dirname(self.path_logs), exist_ok=True)
        formatter = logging.Formatter("[%(asctime)s] [%(pathname)s:%(lineno)d] %(levelname)s - %(message)s")
        handler = TimedRotatingFileHandler(self.path_logs, when='midnight', interval=1, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.DEBUG)
        app.logger.debug('init logger')
