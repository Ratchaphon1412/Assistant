from SpeechToText.speechToText import SpeechTT
from TextToSpeech.textToSpeech import textTTS

class AI:
    def __init__(self):
        self.speechTT = SpeechTT()
        self.textTTS = textTTS()
   


    def mainAI(self):

        while(True):
            
            try:
                
                audio,recognition = self.speechTT.startListen()
                text = self.speechTT.changevoiceTT(audio,recognition)
                if text != None:
                    if(text in "สวัสดี"):
                        self.textTTS.changetextTV("สวัสดีค่ะ")

                print(text)

            except:
                break
        
