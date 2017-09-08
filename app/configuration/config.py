import os
import yaml

class Configuration(object):

  def __init__(self, file_name='base_config.yaml'):
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'r') as stream:
      try:
        self.data = yaml.load(stream)
      except yaml.YAMLError as e:
        print(e)
  
  def app_name(self):
    return self.data['app']['name']

  def flask_debug(self):
    return self.data['flask']['debug']

  def flask_host(self):
    return os.getenv('FLASK_HOST', self.data['flask']['host'])

  def flask_port(self):
    return int(os.getenv('FLASK_PORT', self.data['flask']['port']))
