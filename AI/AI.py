
from html import entities
from SpeechToText.speechToText import SpeechTT
from TextToSpeech.textToSpeech import textTTS
from Knowledge.main import Knowlegde
from .Wit import Wit

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
                if text != None:
                    intent,confidence,entities= self.wit.getIntent(text)
                    if(intent != None):
                        if(confidence >= 0.85):
                            if(intent == "greeting"):
                                self.textTTS.changetextTV("สวัสดีค่ะ")
                            if(intent == "weather"):
                                if(entities == dict()):
                                    # when entities is empty
                                    lat,long = self.knowLedge.getGeoLocation()
                                    des,temp = self.knowLedge.weatherCurrent(lat,long)
                                    text  = self.knowLedge.answerWeather(des,temp)
                                    self.textTTS.changetextTV(text)
                                else:
                                    location = None
                                    #TODO ask location weather
                                    for dic in entities["location:location"]:
                                        max = 0
                                        if  dic["confidence"] >= max:
                                            max = dic["confidence"]
                                            location = dic["value"]
                                    lat,long,name =self.knowLedge.getPlaceGeolocation(location)
                                    des,temp = self.knowLedge.weatherCurrent(lat,long)

                                
                        else:
                            pass
                    else:
                        pass
        


            except:
                break
        
