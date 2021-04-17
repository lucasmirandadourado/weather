from app import app
from flask import request
from app.services.weather import Weather

@app.route("/weather", methods=['POST'])
def findWeather():
    name = request.args.get('city')
    return Weather().getNameCity(name=name)


@app.route("/weather/city")
def findWeatherCity():
    city = request.args.get('name')
    return Weather().getHistory(city)


@app.route("/weather/history")
def findLastDays():
    city = request.args.get('city')
    day_begin = request.args.get('day_begin')
    day_end = request.args.get('day_end')
    return Weather().getHistoryRangeDays(city=city, dayBegin=day_begin, dayEnd=day_end)


@app.route("/weather/history/all")
def findAll():
    city = request.args.get('city')
    return Weather().findAll(city=city)

