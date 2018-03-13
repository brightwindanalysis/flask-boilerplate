from application import app
from application.utils.logger import Logger
import application.api.example_api

logger = Logger("logs/app.log")

logger.init(app)
app.logger.debug('debug main new')
