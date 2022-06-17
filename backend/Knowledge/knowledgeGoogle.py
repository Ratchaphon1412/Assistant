import json
class KnowledgeGoogle:
    def __init__(self,googleAPI):
        self.googleKey = googleAPI
    def findknowledgeGoogle(self,text):
        endpoint = 'https://kgsearch.googleapis.com/v1/entities:search'
        params = {
            'query':text,
        }