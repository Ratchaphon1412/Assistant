import requests
import json
class Weather:
    def __init__(self):
        pass
    def weatherCurrent(self,lat,long):
        apiKey ="f2b10a33ba4535b73fc9845ab9ffef10"
        r =requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&lang=th&appid={apiKey}')
        print(r.text)
        dic = json.loads(r.text)
        
        description = dic["weather"][0]["description"]
        temp = str("{:.2f}".format(dic["main"]["feels_like"]- 273.15))
        
        return description,temp

