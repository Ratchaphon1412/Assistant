import speech_recognition as sr

class SpeechTT:
    def __init__(self):
        pass

    def startListen(self):
        #setup recognizer
        recognition = sr.Recognizer()
        #setup microphone
        microphone = sr.Microphone()
        #setup  a sensitive microphone or microphones  in louder rooms default between 150 and 3500 but it's up  to situation
        recognition.energy_threshold = 3500
        recognition.adjust_for_ambient_noise(microphone,duration=1)
       
