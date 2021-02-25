
from flask import Blueprint
from flask_restx import Api, Resource
from flask_cors import CORS

api_resources = Blueprint("api_resources", __name__)

CORS(api_resources)

authorizations = {
    'apikey':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

api_call = Api(title="AUDIO FILE SERVER API DOC", doc="/doc", description="This was written by Ewanfo Lucky Peter", authorizations=authorizations, security='apikey')

api_call.init_app(api_resources)

#########################################
#AUDIO API NAMESPACE#####
#########################################

audio_file_api_call = api_call.namespace("Audio File Endpoints", path="/")

from app.views import audio_api_resources, errors
