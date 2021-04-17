import requests
import json
from src.repository.connection import Connection
from src.util.ObjectUtil import ObjectUtil


class Weather(object):
    _api = '775147cebec422d82008ee515c536eb7'

    def getNameCity(self, name: str):
        if ObjectUtil.isNone(name) or ObjectUtil.isEmpty(name):
            return {
                       'message': "Informe o nome da Cidade.",
                       'field': 'city'
                   }, 403
        result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={name}&APPID={self._api}')
        if result.status_code == 404:
            return {
                       'message': 'Informe o nome da cidade corretamente',
                       'field': 'city'
                   }, result.status_code
        repository = Connection()
        repository.save(result)
        return json.dumps(result.json()), 201

    def getHistory(self, city: str):
        repository = Connection()
        data = repository.findWeatherByCity(city)
        return data

    def getHistoryRangeDays(self, city: str, dayBegin: str, dayEnd: str):
        if ObjectUtil.isNone(dayBegin) or ObjectUtil.isNone(dayEnd) or ObjectUtil.isNone(city):
            return {
                'message': 'Informe os campos corretamente',
                'fields': ['city', 'day_begin', 'day_end']
            }, 403
        if ObjectUtil.notDate(dayBegin) or ObjectUtil.notDate(dayEnd):
            return {
                       'message': 'Data informada errada (ex: 2021-04-17)',
                       'fields': ['day_begin', 'day_end']
                   }, 403
        return Connection().findLastDays(city=city, dayBegin=dayBegin, dayEnd=dayEnd)

    def findAll(self, city: str):
        if ObjectUtil.isNone(city):
            return {
                'message': 'Informe o nome da cidade corretamente',
                'fields': ['city']
            }, 403
        return Connection().findAll(city)
