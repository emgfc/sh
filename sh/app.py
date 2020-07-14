from flask import Flask, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('settings')
ma = Marshmallow(app)
db = SQLAlchemy(app)


@app.route("/")
def index() -> str:
    return app.send_static_file("index.html")


@app.route("/css/<path:path>")
@app.route("/js/<path:path>")
@app.route("/img/<path:path>")
@app.route("/favicon.ico", defaults={"path": ""})
def handle_static(path: str) -> str:
    return send_from_directory(app.config["STATIC_DIR"], request.path[1:])
