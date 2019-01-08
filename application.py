import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = ['Channel 1', 'Channel 2', 'channel 3']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html", channels = channels)

@app.route("/create_channel", methods = ["POST"])
def create_channel():
    #Get the channel name from the form and add it to the channels array
    channel_name = request.form.get("channel_name")
    channel = channel_name.title()
    if channel in channels:
        message = "Sorry the channel name already exist"
        return render_template("error.html", message = message)
    else:
        channels.append(channel)
    return render_template("welcome.html", channels = channels)



@app.route("/channel/<string:channel_name>")
def channel(channel_name):
    return render_template("channel.html", channel = channel_name)

#am at the part where i need to watch the videos on socket io and finish it, billard you're making madt progress.