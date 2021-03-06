import os
from datetime import timedelta

basedir = os.path.abspath( os.path.dirname(__file__))

class config():
	
	SECRET_KEY = "asdfkjlashdlkfjhlkjasd"
	CORS_HEADERS = 'Content-Type'
	TESTING = True
	
class DevelopmentConfig(config):
	debug = True
	testing = True
	
configuration = {
	'default':config,
	'DevelopmentConfig':DevelopmentConfig
}
