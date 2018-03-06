from app import app
from utils.logger import Logger
import api.example_api

logger = Logger("example.log")

def main():
    logger.init(app)
    app.run()

if __name__ == '__main__':
    main()
