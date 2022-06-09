from gtts import gTTS
from playsound import playsound
import requests
import os

class textTTS:
    def __init__(self):
        pass
    
    def changetextTV(self,text):
        language = 'th'
        voice = gTTS(text=text, lang=language, slow=False)
        voice.save('Voice.mp3')
        playsound('Voice.mp3')
        os.remove('Voice.mp3')
