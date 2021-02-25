from flask import Flask

from config import configuration
from flask_cors import CORS


def create_app(environment):

    app = Flask(__name__)

    CORS(app)

    #Set configuration
    app.config.from_object(configuration[environment])


    #REGISTER API BLUEPRINT
    from app.views import api_resources

    app.register_blueprint(api_resources, url_prefix = '/')

    CORS(app, support_credentials=True, resources={r'/*': {'origins': '*'}})

    return app
