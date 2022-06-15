from playsound import playsound
from gtts import gTTS
import asyncio
import requests
import json
import os


class textTTS:
    def __init__(self,playhtHeader):
        self.playhtHeader = playhtHeader
    
    async def changetextTV(self,text):
        
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
        
        checkConvert = False
        count = 0
        while count < 10:
            response =  requests.post("https://play.ht/api/v1/convert",data=json.dumps(payload),headers=headers,allow_redirects=True)
            dicresponseConvert = json.loads(response.text)
            transcriptID = dicresponseConvert["transcriptionId"]
            responseSound =   requests.get("https://play.ht/api/v1/articleStatus?transcriptionId="+transcriptID,headers=headers,allow_redirects=True)
            dicresponseConvert = json.loads(responseSound.text)
            print(responseSound.text)
            if(dicresponseConvert["converted"] == True):
                urldownloadMP3 = dicresponseConvert["audioUrl"]
                mp3 =   requests.get(urldownloadMP3,allow_redirects=True)
                open('./Sound/Voice.mp3','wb').write(mp3.content)
                playsound('./Sound/Voice.mp3')
                os.remove('./Sound/Voice.mp3')
                checkConvert = True
                break
            count += 1
            
        return checkConvert
        
        

    
    async def speechPleaseWait(self):
        return playsound("./Sound/finddata.mp3")

    async def main(self,text):
        return await asyncio.gather(self.speechPleaseWait(),self.changetextTV(text))

    def dontunderstand(self):
        return playsound("./Sound/don'tunderstand.mp3")
    def nofeature(self):
        return playsound("./Sound/nofeature.mp3")
    def problemPlayht(self):
        return playsound("./Sound/problem.mp3")


        
        
        
        

   
