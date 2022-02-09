"""
Написать свой модуль utils и перенести в него функцию currency_rates()
из предыдущего задания. Создать скрипт, в котором импортировать этот модуль и выполнить
несколько вызовов функции currency_rates(). Убедиться, что ничего лишнего не происходит.
"""


import datetime

from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)  # строка


def currency_rates(valuta):

    content1 = content.split('<Valute ID')
    for row in content1:
        if valuta.upper() in row:
            content1 = row.replace('/', '').split('<Value>')[-2].replace(',', '.')
            today = datetime.date.today()
            print(today.strftime("%d/%m/%Y"), sep=" ", end=" ")
            return content1
