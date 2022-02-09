"""
(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь
к обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая,
когда все файлы находятся в разных папках.
"""

from sys import argv
from itertools import zip_longest

us_ar, ho_ar, out = argv[1:]
# чтобы получить другой список только предоставленных пользователем аргументов
# (но без имени скрипта)

with open(us_ar, 'r', encoding='utf-8') as us:
    with open(ho_ar, 'r', encoding='utf-8') as hobby:
        all_list = zip_longest((' '.join(us_ar.split(',')) for users in us), hobby, fillvalue=None)

        with open(out, 'w', encoding='utf-8') as f:
            #  внутри цикл на автоматическое редактирование и добавление
            for i in all_list:
                print(f"{str(i[0]).strip()}: {str(i[1]).strip()}", file=f)
