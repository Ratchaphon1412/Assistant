
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
                                    entitiesKey = entities.keys()
                                    location = None
                                    # *time not use now 
                                    time = None
                                    for key in list(entitiesKey):
                                        if(key == "location:location"):
                                            for listinlocation in entities["location:location"]:
                                                max = 0
                                                if  listinlocation["confidence"] >= max:
                                                    max = listinlocation["confidence"]
                                                    location = listinlocation["value"]
                                                    
                                        if(key == "time:time"):
                                            for listintime in entities["time:time"]:
                                                max = 0 
                                                if listintime["confidence"]>= max:
                                                    max = listintime["confidence"]
                                                    time = listintime["value"]
                                    if location != None:
                                        lat,long = self.knowLedge.getPlaceGeolocation(location)
                                        des,temp = self.knowLedge.weatherCurrent(lat,long)
                                        text = self.knowLedge.answerPlaceWeather(des,temp,location)
                                    else:
                                        lat,long = self.knowLedge.getGeoLocation()
                                        des,temp = self.knowLedge.weatherCurrent(lat,long)
                                        text = self.knowLedge.answerWeather(des,temp)
                                    
                                    self.textTTS.changetextTV(text)

                        else:
                            text = self.knowLedge.dontUnderStand()
                            self.textTTS.changetextTV(text)
                    else:
                        pass
            except:
                break
        
