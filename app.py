import json
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from datetime import timedelta
from route.route import UserRoute

with open("config/flask.json") as f:
    global Key
    Key = json.load(f)
    f.close()

app = Flask(__name__)

app.config["SECRET_KEY"] = Key["KEY"]
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=5)

app.register_blueprint(UserRoute)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
