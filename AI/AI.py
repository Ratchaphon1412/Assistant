
from html import entities
from SpeechToText.speechToText import SpeechTT
from TextToSpeech.textToSpeech import textTTS
from Knowledge.main import Knowlegde
from .Wit import Wit

class AI:
    def __init__(self,weatherAPI,playhtHeader,witAPI):
        self.speechTT = SpeechTT()
        self.textTTS = textTTS(playhtHeader)
        self.knowLedge = Knowlegde(weatherAPI)
        self.wit = Wit(witAPI)
        



    def mainAI(self):

        while(True):
            
            try:
                
                audio,recognition = self.speechTT.startListen()
                text = self.speechTT.changevoiceTT(audio,recognition)
                print(text)
                if text != None:
                    intent,confidence,entities= self.wit.getIntent(text)
                    if(intent != None):
                        if(confidence >= 0.85):
                            if(intent == "greeting"):
                                self.textTTS.changetextTV("สวัสดีค่ะ")
                            if(intent == "weather"):
                            
                                lat,long = self.knowLedge.getGeoLocation()
                                des,temp = self.knowLedge.weatherCurrent(lat,long)
                                text  = self.knowLedge.answerWeather(des,temp)
                                self.textTTS.changetextTV(text)
                                # test branch
                        else:
                            pass
                    else:
                        pass
        


            except:
                break
        
