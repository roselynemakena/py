class Config(object):
	"""
		Configs - common
	"""

class DevelopmentConfig(object):
	"""
		Configs - Development
	"""

	DEBUG = True
	SQLALCHEMY_ECHO  = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(object):

	"""
		Configs -  Production
	"""

	DEBUG = False

app_config = {
	
	'development': DevelopmentConfig,
	'production': ProductionConfig
}
