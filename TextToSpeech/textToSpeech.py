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
        
        language = 'th'
        voice = gTTS(text=text, lang=language, slow=False)
        voice.save('Voice.mp3')
        playsound('Voice.mp3')
        os.remove('Voice.mp3')
        return
        
        
        
        
        

   
