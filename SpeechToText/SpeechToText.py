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
        #setup default noise
        recognition.adjust_for_ambient_noise(microphone)
        
        #start listen User
        audio = recognition.listen(microphone)
        # change voice to string with Wit api

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + recognition.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
                
        

        


        
       
