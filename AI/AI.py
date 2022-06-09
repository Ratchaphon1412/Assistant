from SpeechToText.speechToText import SpeechTT

class AI:
    def __init__(self):
        self.speechTT=SpeechTT()
        
   


    def mainAI(self):

        while(True):
            
            try:
                
                text =  self.speechTT.startListen()
                print(text)
            except:
                return  
        
