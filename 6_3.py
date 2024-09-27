"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в
файлах во много раз меньше объема ОЗУ. Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""
from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):  # если длина списка users больше hobby
            users.seek(0)  # перемещение указателя в начало
            hobby.seek(0)
            with open('list_users_hobby.json', 'w', encoding='utf-8') as f:
                all_list = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
#  соединение в кортежи. Сначала редактирование строки в users, потом применение в цикле, затем выполнение zip_longest
                new_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}

                dump(new_dict, f, ensure_ascii=False, indent=6)  # запись json, отключение кодировки
            print(new_dict)
        else:
            print(1)
