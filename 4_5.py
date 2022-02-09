"""
* (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

from requests import get, utils
from sys import argv
import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)  # строка


def currency_rates(valuta):

    content1 = content.split('<Valute ID')
    for row in content1:
        if valuta.upper() in row:
            content1 = row.replace('/', '').split('<Value>')[-2].replace(',', '.')
            today = datetime.date.today()
            print(today.strftime("%d-%m-%Y"), sep=" ", end=" ")
            return content1


if __name__ == '__main__':
    word = argv[1]
    print(currency_rates(word))
