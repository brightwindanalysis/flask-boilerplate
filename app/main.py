from app import app
from utils.logger import Logger

logger = Logger("example.log")

def main():
    logger.init(app)
    app.run()

if __name__ == '__main__':
  main()
