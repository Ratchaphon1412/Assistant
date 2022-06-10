from .geolocation import Geolocation
from .nlg import Nlg
from .weather import Weather

class Knowlegde(Geolocation,Nlg,Weather):
    def __init__(self,weatherAPI):
        Geolocation.__init__(self)
        Nlg.__init__(self)
        Weather.__init__(self,weatherAPI)