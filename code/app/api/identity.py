from flask_restful import Resource
from flask import request

class IdentityResource(Resource):
    def get(self):
        return {"identity": "resource"}
    
    def post(self):
        file = request.files.get("file")
        if not file:
            response = {
                "error": "No file provided"
            }
            return response, 400

        response = {
            "status": "success",
            "analysis": {
                "detectedVoice": "true",
                "voiceType": "human",
                "confidenceScore": {
                    "aiProbablity": 5,
                    "humanProbablity": 95
                },
                "additionalInfo": {
                    "emotionalTone":"neutral",
                    "backgroundNoiseLevels":"low"
                }
            },
            "file_name": file.filename,
            "responseTime": 200
        }
        return response, 200
