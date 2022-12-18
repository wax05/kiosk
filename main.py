import json
from flask import Flask ,render_template ,url_for,redirect,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO
from module.Log import Logging
from route.route import UserRoute
from module import DB

with open("./config/sql.json") as f:
    global Set
    Set = json.load(f)
    f.close()

with open("./config/flask.json") as f:
    global Key
    Key = json.load(f)
    f.close()

app = Flask(__name__)
socketio = SocketIO(logger=True,engineio_logger=True)

app.config['SECRET_KEY'] = Key["KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{Set['user']}:{Set['password']}@{Set['host']}:{Set['port']}/{Set['db_name']}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

socketio = SocketIO(app)
db = SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(UserRoute)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)

if __name__ == '__main__':
    socketio.run(app,debug=True)