class Config(object)
	"""
		Configs - common
	"""

class DevelopmentConfig(object)
	"""
		Configs - Development
	"""

	DEBUG = true
	SQLALCHEMY_ECHO  = true


class ProductionConfig(object)

	"""
		Configs -  Production
	"""

	DEBUG = false

app_config = {
	
	'development': DevelopmentConfig,
	'production': ProductionConfig
}
