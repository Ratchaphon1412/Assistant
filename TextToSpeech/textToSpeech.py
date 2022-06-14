from playsound import playsound
from gtts import gTTS
import requests
import json
import os


class textTTS:
    def __init__(self,playhtHeader):
        self.playhtHeader = playhtHeader
    
    def changetextTV(self,text):
        
        headers = {
            'Authorization':self.playhtHeader["Authorization"],
            'X-User-ID':self.playhtHeader["X-User-ID"],
            'Content-Type' : 'application/json'
            }
        payload ={
            'voice':'th-TH-NiwatNeural',
            'content':[text],
            'title': 'test'
        }
        
        try :
            response =  requests.post("https://play.ht/api/v1/convert",data=json.dumps(payload),headers=headers)
            dicresponseConvert = json.loads(response.text)
            transcriptID = dicresponseConvert["transcriptionId"]
            responseSound =  requests.get("https://play.ht/api/v1/articleStatus?transcriptionId="+transcriptID,headers=headers)
            dicresponseConvert = json.loads(responseSound.text)
            urldownloadMP3 = dicresponseConvert["audioUrl"]
            mp3 =  requests.get(urldownloadMP3,allow_redirects=True)
    
            open('Voice.mp3','wb').write(mp3.content)
            playsound('Voice.mp3')
            os.remove('Voice.mp3')
            

        except:
            language = 'th'
            voice = gTTS(text=text, lang=language, slow=False)
            voice.save('Voice.mp3')
            playsound('Voice.mp3')
            os.remove('Voice.mp3')
        return
        
        
        
        
        

   
