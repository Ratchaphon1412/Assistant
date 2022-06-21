import json
import requests
class KnowledgeGoogle:
    def __init__(self,googleAPI):
        self.googleKey = googleAPI
    def findknowledgeGoogle(self,text):
        endpoint = 'https://kgsearch.googleapis.com/v1/entities:search'
        params = {
            'query':text,
            'limit':5,
            'indent':True,
            'key':self.googleKey,
        }
        response = requests.get(endpoint,params=params)
        print(response.text)
        