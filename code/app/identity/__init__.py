import json
from flask import Blueprint, render_template

with open("results.json","r") as f:
    db = json.load(f)

voice_blueprint= Blueprint("voice", __name__,template_folder="templates", url_prefix="/voice")

@voice_blueprint.route("/")
def index():
    return render_template("identity/index.html", results = db)

