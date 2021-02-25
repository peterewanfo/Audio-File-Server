import os
from datetime import timedelta

basedir = os.path.abspath( os.path.dirname(__file__))

class config():
	
	SECRET_KEY = "asdfkjlashdlkfjhlkjasd"
	CORS_HEADERS = 'Content-Type'
	
class ProductionConfig(config):
	debug = False

class DevelopmentConfig(config):
	debug = True
	
configuration = {
	'default':config,
	'ProductionConfig':ProductionConfig,
	'DevelopmentConfig':DevelopmentConfig
}
