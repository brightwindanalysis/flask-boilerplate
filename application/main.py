from application import app
from application.logger import Logger

Logger().init()

# api
import application.api.status_api
import application.api.example_api
