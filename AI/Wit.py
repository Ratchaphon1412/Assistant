from textwrap import indent
import requests
import json
class Wit:
    def __init__(self,witAPI):
        self.witapiKey = witAPI
        self.endpointMessage = "https://api.wit.ai/message?v=20220612&q="


    def getIntent(self,text):
        headers = {
            'Authorization':self.witapiKey
        }
        response = requests.get(self.endpointMessage+text,headers=headers)
        dicresponse = json.loads(response.text)
        
        intent = dicresponse["intents"][0]["name"] 
        confidence = dicresponse["intents"][0]["confidence"] 
        entities = dicresponse["entities"]
        

        return intent,confidence,entities