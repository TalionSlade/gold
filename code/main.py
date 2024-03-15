from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/detection", methods=["POST"])
def analyzeVoice():
    file = request.files.get("file")
    if not file:
        response = {
            "error": "No file provided"
        }
        return jsonify(response), 400

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
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
