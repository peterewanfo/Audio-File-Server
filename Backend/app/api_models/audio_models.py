from app.views import audio_file_api_call
from flask_restx import fields

create_audio_file_model = audio_file_api_call.model("CREATE AUDIO FILE", {
    "file_type":fields.String(description="asdf", example="song"),
    "file_metadata":fields.Raw("file_metadata", example={"name":"Story of My Life", "duration":"248"})
})


update_audio_file_model = audio_file_api_call.model("UPDATE AUDIO FILE", {
    "file_metadata":fields.Raw("file_metadata", example={"name":"Story of My Life", "duration":"248"})
})

get_audio_file_model = audio_file_api_call.model("GET AUDIO FILE", {
    "file_type":fields.String("file_type", required=False)
})
