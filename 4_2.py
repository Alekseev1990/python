"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого
нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре
был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""
from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)  # строка


def currency_rates(valuta):

    content1 = content.split('<Valute ID')
    for row in content1:
        if valuta.upper() in row:
            content1 = row.replace('/', '').split('<Value>')[-2].replace(',', '.')
            return content1


print(currency_rates('AUD'))
print(currency_rates('wtw'))


# chislo = {'AUD': 'Австралийский доллар', 'AZN': 'Азербайджанский манат',
#      'GBP': 'Фунт стерлингов Соединенного королевства', 'AMD': 'Армянских драмов', 'BYN': 'Белорусский рубль',
#      'BGN': 'Болгарский лев', 'BRL': 'Бразильский реал', 'HUF': 'Венгерских форинтов', 'DKK': 'Датская крона',
#      'USD': 'Доллар США', 'EUR': 'Евро', 'INR': 'Индийских рупий', 'KZT': 'Казахстанских тенге',
#      'CAD': 'Канадский доллар', 'KGS': 'Киргизских сомов', 'CNY': 'Китайский юань', 'MDL': 'Молдавских леев',
#      'NOK': 'Норвежских крон', 'PLN': 'Польский злотый', 'RON': 'Румынский лей',
#      'XDR': 'СДР (специальные права заимствования)', 'SGD': 'Сингапурский доллар', 'TJS': 'Таджикских сомони',
#      'TRY': 'Турецких лир', 'TMT': 'Новый туркменский манат', 'UZS': 'Узбекских сумов',
#      'UAH': 'Украинских гривен', 'CZK': '', 'SEK': 'Шведских крон', 'CHF': 'Швейцарский франк',
#      'ZAR': 'Южноафриканских рэндов', 'KRW': 'Вон Республики Корея', 'JPY': 'Японских иен'}

#     row = content.replace('</Value></Valute><Valute', ' ').replace('</Value></Valute></ValCurs>', ' ').\
#     replace('</Name><Value>', ' ').split('  ')
#     for key in row:
#         if key in row:
#             new_content = row[-8:]
#             print(new_content)
#         # return float()
#             #        new_content = row[-8:]
#             #        key = new_content
#             #        return key
#             #
#
# print(currency_rates('USD'))

# for row in content:
# row = content.replace('</Value></Valute><Valute', ' ').replace('</Value></Valute></ValCurs>', ' ').\
# replace('</Name><Value>', ' ').replace('</CharCode><Nominal>1</Nominal><Name>', ' ').\
# replace('</CharCode><Nominal>10</Nominal><Name>', ' ').replace('</CharCode><Nominal>100</Nominal><Name>', ' ').\
# replace('</CharCode><Nominal>1000</Nominal><Name>', ' ').replace('</CharCode><Nominal>10000</Nominal><Name>', ' ').\
# replace('</CharCode><Nominal>10</Nominal><Name>', ' ').replace('NumCode>', ' ').replace('ID="', ' ')
# content1 = row.split('  ')
# # print(content1)
# for key in chislo:
#     if key in row:
#         for row in content1:
#             new_content = row[-8:]
#         return new_content
