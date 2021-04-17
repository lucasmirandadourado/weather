import json

import psycopg2
from src.model.weather import Weather
from src.util.ObjectUtil import ObjectUtil
from datetime import datetime


class Connection:

    def save(self, data):
        weather = self.convertJsonToWeather(data)

        sql = """ SET TIMEZONE TO 'America/Sao_Paulo'; INSERT INTO weather
            (coord_lon, coord_lat, temp, feels_like, 
            temp_min, temp_max, pressure, humidity, 
            sea_level, grnd_level, visibility, wind_speed, 
            wind_deg, wind_gust, clouds_all, country, 
            sunrise, sunset, city, dt)
            VALUES(%s, %s, %s, %s, 
            %s, %s, %s, %s, 
            %s, %s, %s, %s,
            %s, %s, %s, %s, 
            %s, %s, %s, %s); """

        content = (weather.getCoordLon(), weather.getCoordLat(), weather.getTemp(), weather.getFeelsLike(),
                   weather.getTempMin(), weather.getTempMax(), weather.getPressure(), weather.getHumidity(),
                   weather.getSeaLevel(), weather.getGrndLevel(), weather.getVisibility(), weather.getWindSpeed(),
                   weather.getWindDeg(), weather.getWindGust(), weather.getCloudsAll(), weather.getCountry(),
                   weather.getSunrise(), weather.getSunset(), weather.getCity(), weather.getDt())

        connection = self.__getConnection()
        cursor = connection.cursor()
        cursor.execute(sql, content)
        connection.commit()

    def findWeatherByCity(self, city: str):
        try:
            sql = "SELECT * FROM weather where city ilike '%{}%'".format(city)
            connection = self.__getConnection()
            cursor = connection.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            list = self.convert(res)
            total = len(list)
            resp = {
                'city': city,
                'total': total,
                'data': list
            }
            return json.dumps(resp)

        except (Exception, psycopg2.Error) as error:
            print(f"Error na busca do histórico: ({error})")
            raise

    def convert(self, res):
        list = []
        for item in res:
            weather = {
                "id": item[0],
                "coordLon": str(item[1]),
                "coordLat": str(item[2]),
                "temp": str(item[3]),
                "feelsLike": str(item[4]),
                "tempMin": float(item[5]) - 273,
                "tempMax": float(item[6]) - 273,
                "pressure": str(item[7]),
                "humidity": str(item[8]),
                "seaLevel": str(item[9]),
                "grndLevel": str(item[10]),
                "visibility": str(item[11]),
                "windSpeed": str(item[12]),
                "windDeg": str(item[13]),
                "windGust": str(item[14]),
                "cloudsAll": str(item[15]),
                "country": str(item[16]),
                "sunrise": str(item[17]),
                "sunset": str(item[18]),
                "city": str(item[19]),
                "dt": str(item[20]),
            }
            list.append(weather)
        return list

    def convertJsonToWeather(self, data):
        weather = Weather()
        for key, value in data.json().items():
            if ObjectUtil.existField(key, 'coord'):
                if ObjectUtil.existField(value, 'lat'):
                    weather.setCoordLat(value['lat'])
                if ObjectUtil.existField(value, 'lon'):
                    weather.setCoordLon(value['lon'])
            if ObjectUtil.existField(key, 'main'):
                if ObjectUtil.existField(value, 'temp'):
                    weather.setTemp(value['temp'])
                if ObjectUtil.existField(value, 'feels_like'):
                    weather.setFeelsLike(value['feels_like'])
                if ObjectUtil.existField(value, 'temp_max'):
                    weather.setTempMax(value['temp_max'])
                if ObjectUtil.existField(value, 'temp_min'):
                    weather.setTempMin(value['temp_min'])
                if ObjectUtil.existField(value, 'pressure'):
                    weather.setPressure(value['pressure'])
                if ObjectUtil.existField(value, 'humidity'):
                    weather.setHumidity(value['humidity'])
                if 'sea_level' in value:
                    weather.setSeaLevel(value['sea_level'])
                if 'grnd_level' in value:
                    weather.setGrndLevel(value['grnd_level'])
            if ObjectUtil.existField(key, 'visibility'):
                weather.setVisibility(value)
            if ObjectUtil.existField(key, 'wind'):
                if ObjectUtil.existField(value, 'speed'):
                    weather.setWindSpeed(value['speed'])
                if ObjectUtil.existField(value, 'deg'):
                    weather.setWindDeg(value['deg'])
                if ObjectUtil.existField(value, 'gust'):
                    weather.setWindGust(value['gust'])
            if ObjectUtil.existField(key, 'clouds'):
                weather.setCloudsAll(value['all'])
            if ObjectUtil.existField(key, 'dt'):
                weather.setDt(datetime.utcfromtimestamp(value))
            if ObjectUtil.existField(key, 'sys'):
                if ObjectUtil.existField(value, 'country'):
                    weather.setCountry(value['country'])
                if ObjectUtil.existField(value, 'sunrise'):
                    weather.setSunrise(datetime.utcfromtimestamp(value['sunrise']))
                if ObjectUtil.existField(value, 'sunset'):
                    weather.setSunset(datetime.utcfromtimestamp(value['sunset']))
            if ObjectUtil.existField(key, 'timeszone'):
                weather.setTimezone(value)
            if ObjectUtil.existField(key, 'name'):
                weather.setCity(value)
        return weather

    def findLastDays(self, city: str, dayBegin: str, dayEnd: str):
        try:
            sql = '''SELECT * FROM weather 
            where city ilike '%{}%' 
            and dt::timestamp between '{}'::timestamp and '{} 23:59:59'::timestamp'''.format(city, dayBegin, dayEnd)
            connection = self.__getConnection()
            cursor = connection.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            list = self.convert(res)
            total = len(list)
            resp = {
                'city': city,
                'date_begin': dayBegin,
                'date_end': dayEnd,
                'total': total,
                'data': list
            }
            return json.dumps(resp)

        except (Exception, psycopg2.Error) as error:
            print(f"Error na busca do histórico: ({error})")
            raise

    def __getConnection(self):
        return psycopg2.connect(user='root',
                                password='root',
                                host='localhost',
                                port=5432,
                                database='wearther')
