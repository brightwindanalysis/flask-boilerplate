from flask import Flask
from config import Configuration

configuration = Configuration()
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
  return "hello world"

if __name__ == '__main__':
  app.logger.debug('start application: %s', configuration.app_name)
  #app.run(host='0.0.0.0', debug=True)
