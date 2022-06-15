from cgitb import text
from .geolocation import Geolocation
from .nlg import Nlg
from .weather import Weather

class Knowlegde(Geolocation,Nlg,Weather):
    def __init__(self,weatherAPI,rapidAPI):
        Geolocation.__init__(self,rapidAPI)
        Nlg.__init__(self)
        Weather.__init__(self,weatherAPI)

    def weather(self,entities):
        text = None
        if(entities == None):
            # when entities is empty
            lat,long = self.getGeoLocation()
            des,temp = self.weatherCurrent(lat,long)
            text  = self.answerWeather(des,temp)  
        else:
            entitiesKey = entities.keys()
            location = None
            # *time not use now 
            time = None
            for key in list(entitiesKey):
                if(key == "location:location"):
                    for listinlocation in entities["location:location"]:
                        max = 0
                        if  listinlocation["confidence"] >= max:
                            max = listinlocation["confidence"]
                            location = listinlocation["value"]
                            
                if(key == "time:time"):
                    for listintime in entities["time:time"]:
                        max = 0 
                        if listintime["confidence"]>= max:
                            max = listintime["confidence"]
                            time = listintime["value"]
            if location != None:
                lat,long = self.getPlaceGeolocation(location)
                des,temp = self.weatherCurrent(lat,long)
                text = self.answerPlaceWeather(des,temp,location)
            else:
                lat,long = self.getGeoLocation()
                des,temp = self.weatherCurrent(lat,long)
                text = self.answerWeather(des,temp)
        return text  
                