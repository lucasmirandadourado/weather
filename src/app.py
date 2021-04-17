from flask import Flask, request
from src.services.weather import Weather

app = Flask("Weather")


@app.route("/weather", methods=['POST'])
def findWeather():
    name = request.args.get('city')
    return Weather().getNameCity(name=name)


@app.route("/weather/city")
def findWeatherCity():
    city = request.args.get('city')
    return Weather().getHistory(city)

@app.route("/weather/history")
def findLastDays():
    city = request.args.get('city')
    day_begin = request.args.get('day_begin')
    day_end = request.args.get('day_end')
    return Weather().findLastDays(city=city, dayBegin=day_begin, dayEnd=day_end)

@app.route("/weather/history/all")
def findAll():
    city = request.args.get('city')
    return Weather().findAll(city=city)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
