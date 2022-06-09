from geopy.geocoders import Nominatim
import geocoder

class  Geolocation:
    def __init__(self):
        pass
    def getGeoLocation(self):
        Nomi_locator = Nominatim(user_agent="My App")
        my_location= geocoder.ip('me')

        #my latitude and longitude coordinates
        latitude= my_location.geojson['features'][0]['properties']['lat']
        longitude = my_location.geojson['features'][0]['properties']['lng']
        return latitude,longitude




