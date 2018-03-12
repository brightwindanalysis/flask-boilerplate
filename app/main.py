from flask import Flask

app = Flask(__name__)

#import app.api.example_api

from app.utils.logger import Logger
logger = Logger("logs/app.log")
logger.init(app)
app.logger.debug('A value for debugging')

'''
from utils.logger import Logger
import api.example_api

logger = Logger("example.log")

def main():
    logger.init(app)
    app.run()

if __name__ == '__main__':
    main()
'''