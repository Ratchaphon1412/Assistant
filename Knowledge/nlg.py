import random
class Nlg:
    def __init__(self):
        pass
    def answerWeather(self,des,temp):
        mergeString = ["มี"," สภาพอากาศที่คุณอยู่ มี","ณ ที่คุณอยู่ มี"]
        text = mergeString[random.randrange(0,2)] + des + " อุณหภูมิประมาณ "+temp
        return text
      
