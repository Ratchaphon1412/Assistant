from crypt import methods
from AI.AI import AI
import json
from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'AISecretKey'
socketio = SocketIO(app)


@app.route("/")
def getWeather():
    return "<p>Test</p>"


if __name__ == '__main__':

    socketio.run(app)

    with open('key.json')as fileJson:
        key = json.load(fileJson)
        weatherAPI = key["APIKEY"]["weatherAPI"]
        playhtHeader = key["APIKEY"]["play.htAPI"]
        witAPI = key["APIKEY"]["witAPI"]
        rapidAPI = key["APIKEY"]["rapidAPI"]
        googleAPI = key["APIKEY"]["googleAPI"]
        googleMapAPI = key["APIKEY"]["googleMapAPI"]
    ai = AI(weatherAPI, playhtHeader, witAPI,
            rapidAPI, googleAPI, googleMapAPI)
    ai.mainAI()
