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
            'languages':'th'
        }
        response = requests.get(endpoint,params=params)
        print(response.text)
        articleList = []
        listData = json.loads(response.text)
        if (len(listData['itemListElement']) != 0):
            for diclist in listData['itemListElement']:
                if('result' in diclist):
                    if('detailedDescription' in diclist['result']):
                        if('articleBody'in diclist['result']['detailedDescription']):
                            articleList.append(diclist['result']['detailedDescription']['articleBody'])
        
        return articleList


                



        