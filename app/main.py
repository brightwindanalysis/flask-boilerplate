from app import app
from configuration.config import Configuration
import routes
import os
import yaml

configuration = Configuration()

if __name__ == '__main__':
  print('start application: {0}'.format(configuration.app_name()))
  app.run(host=configuration.flask_host(), port=configuration.flask_port(), debug=configuration.flask_debug())
