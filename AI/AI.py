
from SpeechToText.speechToText import SpeechTT
from TextToSpeech.textToSpeech import textTTS
from Knowledge.main import Knowlegde

class AI:
    def __init__(self,weatherAPI):
        self.speechTT = SpeechTT()
        self.textTTS = textTTS()
        self.knowLedge = Knowlegde(weatherAPI)



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
                       
                        lat,long = self.knowLedge.getGeoLocation()
                        des,temp = self.knowLedge.weatherCurrent(lat,long)
                        text  = self.knowLedge.answerWeather(des,temp)
                        self.textTTS.changetextTV(text)
                        # test branch
            except:
                break
        
