from app import app
from configuration.config import Configuration
import routes

configuration = Configuration()

if __name__ == '__main__':
  print('start application: %s', configuration.app_name)
  #app.run(host='0.0.0.0', debug=True)
