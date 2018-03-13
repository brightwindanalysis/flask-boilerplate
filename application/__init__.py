from flask import Flask

app = Flask(__name__)
app.config.from_object('application.configuration.DevConfig')
#app.config.from_envvar('APPLICATION_SETTINGS', silent=True)

import application.main
