from fileinput import close
import random
class Nlg:
    def __init__(self):
        pass
    def answerWeather(self,des,temp):
        mergeString = ["มี"," สภาพอากาศที่คุณอยู่ มี","ณ ที่คุณอยู่ มี"]
        speechtemp = [""," อุณหภูมิประมาณ " + temp + "องศา"]
        if "ฝน" in des:
            text = mergeString[random.randrange(0,2)] + des + speechtemp[random.randrange(0,2)] + "กรุณาเอาพกร่มไปด้วย"
        else:
            text = mergeString[random.randrange(0,2)] + des + speechtemp[random.randrange(0,2)]
        return text
      
