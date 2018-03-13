from application import app
from application.logger import Logger

Logger().init()

# api
import application.api.status_api
import application.api.example_api

# if run with cli this is NOT executed
if __name__ == '__main__':
    app.logger.info('start application: [{0}] @ {1}:{2} in DEBUG={3}'.format(
        app.config['APP_NAME'], app.config['HOST'], app.config['PORT'], app.config['DEBUG']))
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
