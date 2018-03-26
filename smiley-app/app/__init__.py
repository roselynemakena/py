

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_migrate import Migrate


from config import app_config

db = SQLAlchemy()
lm = LoginManager()


def create_app(config_name):

	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)

	lm.init_app(app)
	lm.login_message = "You must be logged in to view this page"
	lm.login_view = "auth.login"

	migrate = Migrate(app, db)
	from app import models

	@app.route('/')
	def hello_peeps():
		return 'Hi people of the world...eureka!'

	return app



