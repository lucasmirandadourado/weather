import psycopg2
from src.model.weather import Weather


class Connection:

    def save(self, data):
        weather = self.convertJsonToWeather(data)

        sql = """ INSERT INTO public.weather
        (coord_lon, coord_lat, temp, feels_like, temp_min,
         temp_max, pressure, humidity, sea_level, grnd_level,
         visibility, wind_speed, wind_deg, wind_gust,
         clouds_all, country, sunrise, sunset, city)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """

        content = (weather.getCoordLon(), weather.getCoordLat(), weather.getTemp(), weather.getFeelsLike(),
                   weather.getTempMin(),
                   weather.getTempMax(), weather.getPressure(), weather.getHumidity(), weather.getSeaLevel(),
                   weather.getGrndLevel(),
                   weather.getVisibility(), weather.getWindSpeed(), weather.getWindDeg(), weather.getWindGust(),
                   weather.getCloudsAll(), weather.getCountry(), weather.getSunrise(), weather.getSunset(),
                   weather.getCity())

        connection = self.__getConnection()
        cursor = connection.cursor()
        cursor.execute(sql, content)
        connection.commit()

    def convertJsonToWeather(self, data):
        weather = Weather()
        for key, value in data.json().items():
            print(key, value)
            if key == 'coord':
                weather.setCoordLat(float(value['lat']))
                weather.setCoordLon(float(value['lon']))
            if key == 'main':
                weather.setTemp(value['temp'])
                weather.setFeelsLike(value['feels_like'])
                weather.setTempMax(value['temp_max'])
                weather.setTempMin(value['temp_min'])

                weather.setPressure(value['pressure'])
                weather.setHumidity(value['humidity'])
                if 'sea_level' in value:
                    weather.setSeaLevel(value['sea_level'])
                if 'grnd_level' in value:
                    weather.setGrndLevel(value['grnd_level'])
            if key == 'visibility':
                weather.setVisibility(value)
            if key == 'wind':
                weather.setWindSpeed(value['speed'])
                weather.setWindDeg(value['deg'])
                weather.setWindGust(value['gust'])
            if key == 'clouds':
                weather.setCloudsAll(value['all'])
            if key == 'dt':
                weather.setCloudsAll(value)
            if key == 'sys':
                weather.setCountry(value['country'])
                weather.setSunrise(value['sunrise'])
                weather.setSunset(value['sunset'])
            if key == 'timeszone':
                weather.setTimezone(value)
            if key == 'name':
                weather.setCity(value)
        return weather

    def __getConnection(self):
        return psycopg2.connect(user='root',
                                     password='root',
                                     host='localhost',
                                     port=5432,
                                     database='wearther')

