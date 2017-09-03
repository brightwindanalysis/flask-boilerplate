import os
import yaml

class Configuration(object):

  def __init__(self, file_name='base_config.yaml'):

    print(os.listdir(os.path.dirname(os.path.realpath(__file__))))
    print(os.path.dirname(os.path.realpath(__file__)))
    print('{0}'.format(os.path.isfile(file_name)))
    print('{0}'.format(os.path.exists(file_name)))

    with os.open(file_name, os.O_RDONLY) as stream:
      try:
        self['data'] = yaml.load(stream)
        print(self[data])
      except yaml.YAMLError as e:
        print(e)
  
  def __data(self):
    return self['data']

  def app_name(self):
    return __data()['app']['name']

  def flask_debug(self):
    return __data()['flask']['debug']

  def flask_host(self):
    return os.getenv('FLASK_HOST', __data()['flask']['host'])

  def flask_port(self):
    return os.getenv('FLASK_PORT', __data()['flask']['port'])
