from fileinput import close
import random
class Nlg:
    def __init__(self):
        pass
    def answerWeather(self,des,temp):
        mergeString = ["มี"," สภาพอากาศที่คุณอยู่ มี","ณ ที่คุณอยู่ มี"]
        speechtemp = [""," อุณหภูมิประมาณ " + temp + "องศา"]
        speech = None
        if "ฝน" in des:
            speech = mergeString[random.randrange(0,2)] + des + speechtemp[random.randrange(0,1)] + "อย่าลืมพกร่มไปด้วยนะครับ"
        else:
            speech = mergeString[random.randrange(0,2)] + des + speechtemp[random.randrange(0,1)] + "ครับ"
        print(speech)
        return speech
    
    def answerPlaceWeather(self,des,temp,text):
        mergeString = ["จากที่ทราบข้อมูล แถวๆ บริเวณ ","บริเวณ ","จากข้อมูลพบว่า แถวนั้น "]
        desMerge = ["มี","สภาพอากาศ มี"]
        speechtemp = [""," อุณหภูมิประมาณ " + temp + "องศา"]
        
        if "ฝน" in des:
            speech = mergeString[random.randrange(0,2)] + text  + desMerge[random.randrange(0,1)] + des + speechtemp[random.randrange(0,1)] + "อย่าลืมพกร่มไปด้วยนะครับ"
        else:
            speech = mergeString[random.randrange(0,2)] + text  + desMerge[random.randrange(0,1)] + des + speechtemp[random.randrange(0,1)] + "ครับ"
        
        print(speech)
        return speech

    def dontUnderStand(self):
        speech = "ขอโทษนะครับ ผมไม่ค่อยเข่้าใจ"
        return speech 
    def noFeature(self):
        speech = "ขอโทษด้วยครับ พอดียังไม่มีฟังชั่นนี้ครับ"
        return speech

