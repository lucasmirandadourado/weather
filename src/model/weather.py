class Weather(object):

    def __init__(self):
        self.__coordLon: float = None
        self.__coordLat: float = None
        self.__temp: float = None
        self.__feelsLike: float = None
        self.__tempMin: float = None
        self.__tempMax: float = None
        self.__pressure: float = None
        self.__humidity: float = None
        self.__seaLevel: float = None
        self.__grndLevel: float = None
        self.__visibility: float = None
        self.__windSpeed: float = None
        self.__windDeg: float = None
        self.__windGust: float = None
        self.__cloudsAll: float = None
        self.__dt: float = None
        self.__country: float = None
        self.__sunrise: float = None
        self.__sunset: float = None
        self.__timezone: float = None
        self.__id: float = None
        self.__city: str = None

    def getCoordLon(self):
        return self.__coordLon

    def setCoordLon(self, lon: float):
        self.__coordLon = lon

    def getCoordLat(self):
        return self.__coordLat

    def setCoordLat(self, lat: float):
        self.__coord_lat = lat

    def getTemp(self):
        return self.__temp

    def setTemp(self, temp: float):
        self.__temp = temp

    def getFeelsLike(self):
        return self.__feelsLike

    def setFeelsLike(self, feels):
        self.__feelsLike = feels

    def getTempMin(self):
        return self.__tempMin

    def setTempMin(self, min):
        self.__tempMin = min

    def getTempMax(self):
        return self.__tempMax

    def setTempMax(self, max):
        self.__tempMax = max

    def getPressure(self):
        return self.__pressure

    def setPressure(self, pressure):
        self.__pressure = pressure

    def getHumidity(self):
        return self.__humidity

    def setHumidity(self, humidity):
        self.__humidity = humidity

    def getSeaLevel(self):
        return self.__seaLevel

    def setSeaLevel(self, sea):
        self.__seaLevel = sea

    def getGrndLevel(self):
        return self.__grndLevel

    def setGrndLevel(self, grnd):
        self.__grndLevel = grnd

    def getVisibility(self):
        return self.__visibility

    def setVisibility(self, visibility):
        self.__visibility = visibility

    def getWindSpeed(self):
        return self.__windSpeed

    def setWindSpeed(self, wind):
        self.__windSpeed = wind

    def getWindDeg(self):
        return self.__windDeg

    def setWindDeg(self, deg):
        self.__windDeg = deg

    def getWindGust(self):
        return self.__windGust

    def setWindGust(self, gust):
        self.__windGust = gust

    def getCloudsAll(self):
        return self.__cloudsAll

    def setCloudsAll(self, all):
        self.__cloudsAll = all

    def getDt(self):
        return self.__dt

    def setDt(self, dt):
        self.__dt = dt

    def getCountry(self):
        return self.__country

    def setCountry(self, country):
        self.__country = country

    def getSunrise(self):
        return self.__sunrise

    def setSunrise(self, sunrise):
        self.__sunrise = sunrise

    def getSunset(self):
        return self.__sunset

    def setSunset(self, sunset):
        self.__sunset = sunset

    def getTimezone(self):
        return self.__timezone

    def setTimezone(self, times):
        self.__timezone = times

    def getCity(self):
        return self.__city

    def setCity(self, city):
        self.__city = city
