import speech_recognition as sr

class SpeechTT:
    def __init__(self,witkeyAPI):
        self.keyAPI = witkeyAPI

    def startListen(self):
        #setup recognizer
        recognition = sr.Recognizer()
        #setup microphone
        microphone = sr.Microphone()
        #setup  a sensitive microphone or microphones  in louder rooms default between 150 and 3500 but it's up  to situation
        recognition.energy_threshold = 3500
        #setup default noise
        recognition.adjust_for_ambient_noise(microphone,duration=1)
        #start listen User
        audio = recognition.listen(microphone)
        # change voice to string with Wit api
       
        try:
            return recognition.recognize_wit(audio,key=self.keyAPI)
        except sr.UnknownValueError:
            return "Wit.ai could not understand audio"
        except sr.RequestError as e:
            return "Error"
        

        


        
       
