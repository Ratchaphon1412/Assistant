
from html import entities
from SpeechToText.speechToText import SpeechTT
from TextToSpeech.textToSpeech import textTTS
from Knowledge.main import Knowlegde
from .Wit import Wit
import asyncio

class AI:
    def __init__(self,weatherAPI,playhtHeader,witAPI,rapidAPI):
        self.speechTT = SpeechTT()
        self.textTTS = textTTS(playhtHeader)
        self.knowLedge = Knowlegde(weatherAPI,rapidAPI)
        self.wit = Wit(witAPI)
        



    def mainAI(self):

        while(True):
            try:
                audio,recognition = self.speechTT.startListen()
                text = self.speechTT.changevoiceTT(audio,recognition)
                print(text)
                checkConvertPlayht = None
                if text != None:
                    intent,confidence,entities= self.wit.getIntent(text)
                    if(intent != None):
                        if(confidence >= 0.85):
                            if(intent == "greeting"):
                                    checkConvertPlayht = asyncio.run(self.textTTS.changetextTV("สวัสดีครับ"))
                            if(intent == "weather"):
                               text = self.knowLedge.weather(entities)
                               checkConvertPlayht = asyncio.run(self.textTTS.main(text))
                               self.checkConvertPlayht(checkConvertPlayht)
                        else:
                            self.textTTS.dontunderstand()
                    else:
                        self.textTTS.nofeature()
            except:
                break
    
    def checkConvertPlayht(self,check):
        if check[1] == False:
            self.textTTS.problemPlayht()
        return
                


