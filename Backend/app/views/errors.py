from . import api_resources
from flask import request, jsonify, make_response

@api_resources.app_errorhandler(404)
def error_handler(e):

    return make_response(jsonify({"message": 'Bad Request' } ), 400)