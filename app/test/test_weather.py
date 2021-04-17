import json
import unittest
from app.services.weather import Weather


class TestApiWeather(unittest.TestCase):

    def test_get_data(self):
        data = Weather().getNameCity(name='João Dourado')
        self.assertEqual(2, len(data))
        self.assertEqual(201, data[1])

    def test_buscar_com_valor_none(self):
        data = Weather().getNameCity(name=None)
        self.assertEqual(({'field': 'city', 'message': 'Informe o nome da Cidade.'}, 403), data)

    def test_buscar_com_valor_em_branco(self):
        data = Weather().getNameCity(name='')
        self.assertEqual(({'field': 'city', 'message': 'Informe o nome da Cidade.'}, 403), data)

    def test_buscar_cidade_nao_exist(self):
        data = Weather().getNameCity(name='essa_cidade_nao_existe')
        self.assertEqual(({'field': 'city', 'message': 'Informe o nome da cidade corretamente'}, 404), data)

    def test_buscar_historico(self):
        data = Weather().getHistory(city='Joao Dourado')
        x = json.loads(data)
        self.assertEqual('Joao Dourado', x['city'])
        self.assertEqual(0, x['total'])

        data = Weather().getHistory(city='João Dourado')
        x = json.loads(data)
        self.assertEqual('João Dourado', x['city'])
        self.assertTrue(x['total'] > 0)

    def test_buscar_registros_no_periodo(self):
        data = Weather().getHistoryRangeDays(city=None, dayBegin=None, dayEnd=None)
        message_expected = ({'fields': ['city', 'day_begin', 'day_end'], 'message': 'Informe os campos corretamente'}, 403)
        self.assertEqual(message_expected, data)

        data = Weather().getHistoryRangeDays(city="João Dourado", dayBegin='2021-01-16', dayEnd=None)
        self.assertEqual(
            ({'fields': ['city', 'day_begin', 'day_end'], 'message': 'Informe os campos corretamente'}, 403), data)

        data = Weather().getHistoryRangeDays(city="João Dourado", dayBegin='a', dayEnd='2021-04-17')
        self.assertEqual(
            ({'fields': ['day_begin', 'day_end'], 'message': 'Data informada errada (ex: 2021-04-17)'}, 403), data)

        data = Weather().getHistoryRangeDays(city="João Dourado", dayBegin='2021-01-16', dayEnd='A')
        self.assertEqual(
            ({'fields': ['day_begin', 'day_end'], 'message': 'Data informada errada (ex: 2021-04-17)'}, 403), data)


if __name__ == '__main__':
    unittest.main()
