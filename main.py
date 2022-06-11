from AI.AI import AI
import json


if __name__ == '__main__':
    with open ('key.json')as fileJson:
        key = json.load(fileJson)
        weatherAPI = key["APIKEY"]["weatherAPI"]
        playhtHeader = key["APIKEY"]["play.htAPI"]
    ai = AI(weatherAPI,playhtHeader)
    ai.mainAI()
