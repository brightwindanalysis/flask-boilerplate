from application import app
from application.utils.logger import Logger

import application.api.status_api
import application.api.example_api

Logger("logs/app.log").init(app)
