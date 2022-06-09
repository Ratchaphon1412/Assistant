
from SpeechToText.speechToText import SpeechTT
from TextToSpeech.textToSpeech import textTTS
from  Knowledge.geolocation import Geolocation
from Knowledge.weather import Weather
from Knowledge.nlg  import Nlg
class AI:
    def __init__(self):
        self.speechTT = SpeechTT()
        self.textTTS = textTTS()
        self.geoLocation = Geolocation()
        self.weather = Weather()
        self.nlg = Nlg()


    def mainAI(self):

        while(True):
            
            try:
                
                audio,recognition = self.speechTT.startListen()
                text = self.speechTT.changevoiceTT(audio,recognition)
                print(text)
                if text != None:
                    if(text in "สวัสดี"):
                        self.textTTS.changetextTV("สวัสดีค่ะ")
                    if(text in "สภาพอากาศเป็นยังไง"):
                        lat,long = self.geoLocation.getGeoLocation()
                        des,temp = self.weather.weatherCurrent(lat,long)
                        text  = self.nlg.answerWeather(des,temp)
                        self.textTTS.changetextTV(text)

            except:
                break
        
