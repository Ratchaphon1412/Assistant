from email.mime import audio
from SpeechToText.speechToText import SpeechTT

class AI:
    def __init__(self):
        self.speechTT=SpeechTT()
        
   


    def mainAI(self):

        while(True):
            
            try:
                
                audio,recognition = self.speechTT.startListen()
                text = self.speechTT.changevoiceTT(audio,recognition)
                if text != None:
                    pass
                print(text)

            except:
                break
        
