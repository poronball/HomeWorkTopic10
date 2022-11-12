"""
ЗАДАНИЕ 3

Классы эквивалентности
Позитивные:
           format = 'full' expected = True
           format = 'value' expected = True
Негативные:
           format = 'full' expected = False
           format = 'value' expected = False

тесты должны покрывать все возможные варианты инициализации класса разными значениями переданных аргументов (format='full'/'value', diff=True/False)
"""
import pytest
from unittest.mock import patch, Mock, MagicMock

@pytest.mark.parametrize("arg_format, Valute, expected", [('full','EUR', True), ('value','EUR', True), ('full','asdf', False), ('xcbv','', False)])
def test_init(arg_format, Valute, expected):
    assert init(arg_format,Valute) == expected
    return expected

class Rate:
    """

    """

    def __init__(self, format_='value'):
        self.format = format_

    def exchange_rates(self):
        mock = MagicMock()
        self.r = mock.retreturn_value= {'EUR': {'ID': 'R01239',
  'NumCode': '978',
  'CharCode': 'EUR',
  'Nominal': 1,
  'Name': 'Евро',
  'Value': 61.5416,
  'Previous': 61.0037}}
        return self.r

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }

        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']

        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')

def init(arg_format, Valute):
    t_init = Rate(arg_format)
    t_init.make_format(Valute)
    expected = True
    if arg_format == 'full':
        expected = True
    else:
        expected = False
    if Valute == 'EUR':
        expected = True
    else:
        expected = False
    return expected


