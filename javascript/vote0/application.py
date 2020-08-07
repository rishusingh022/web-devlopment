#build an app on which different  people on different tabs cast vot and same time we
#can see that cast vote on our tab also immmeadiately
import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit#socket io let us do things like real time 
#communication chatting types

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")#when socketio detect this event run this code
def vote(data):
    selection = data["selection"]
    emit("announce vote", {"selection": selection}, broadcast=True)
