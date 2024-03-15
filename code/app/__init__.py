from flask import Flask, render_template
from .identity import voice_blueprint
from .api.identity import IdentityResource
from flask_restful import Api

app = Flask (__name__)
api = Api(app, prefix="/api")

api.add_resource(IdentityResource, "/voice")
app.register_blueprint(voice_blueprint)

@app.route("/")
def index():
    return render_template("index.html")