"""
* (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
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


if __name__ == '__main__':
    print(currency_rates('AUD'))

import utils_homework
print(utils_homework.currency_rates('usd'))
# сначала выдает результат из модуля, потом значение из импорта в главный файл
