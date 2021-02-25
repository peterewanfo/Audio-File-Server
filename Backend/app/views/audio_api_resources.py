from app.business_logic.utils.Decorators import manage_db_connection

from flask import request, jsonify, make_response, json, url_for
import jwt, traceback, time, datetime
from flask_restx import Resource
from app.business_logic.logic.AudioFileClass import AudioFileClass

from app.views import audio_file_api_call
from app.api_models.audio_models import create_audio_file_model, update_audio_file_model, get_audio_file_model

@audio_file_api_call.route('/create')
class CreateNewFile(Resource):
    @staticmethod
    @manage_db_connection
    @audio_file_api_call.expect(create_audio_file_model)
    def post():
        try:

            json_data = request.get_json()

            file_type = json_data["file_type"]
            file_metadata = json_data["file_metadata"]

            data = AudioFileClass.createAudioFile(file_type = file_type, file_metadata = file_metadata)

            return jsonify({'message': data})

        except Exception as e:

            return make_response(jsonify({"message": 'Internal Server Error' } ), 500)


@audio_file_api_call.route('/<file_type>/<file_id>')
class DeleteFile(Resource):
    @staticmethod
    @manage_db_connection
    def delete(file_type, file_id):
        try:

            data = AudioFileClass.deleteAudioFile(file_type = file_type, id = file_id)

            return jsonify({'message': data})

        except Exception as e:

            return make_response(jsonify({"message": 'Internal Server Error' } ), 500)

    @staticmethod
    @manage_db_connection
    @audio_file_api_call.expect(update_audio_file_model)
    def put(file_type, file_id):
        try:

            json_data = request.get_json()

            file_metadata = json_data["file_metadata"]

            data = AudioFileClass.updateAudioFile(file_type = file_type, file_metadata = file_metadata, id = file_id)

            return jsonify({'message': data})

        except Exception as e:

            return make_response(jsonify({"message": 'Internal Server Error' } ), 500)


    @staticmethod
    @manage_db_connection
    @audio_file_api_call.doc(model=get_audio_file_model)
    def get(file_type, file_id):
        try:
            
            data = AudioFileClass.getAudioFile(file_type = file_type, file_id = file_id)

            return jsonify({'message': data})

        except Exception as e:

            return make_response(jsonify({"message": 'Internal Server Error' } ), 500)