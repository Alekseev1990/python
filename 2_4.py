"""
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?
"""


def print_sep(sep):
    print(sep * 150)


#4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:

#Сначала не так понял, что нужно вывести. Пусть останется тут)
text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in text:
    # name = item.split()[-1]
    new_text = item.rsplit(' ', 1)[0] + ' ' + str.capitalize(item.split()[-1])
    print(f" Добрый день, {new_text}!")

print_sep('-')

#variant 1

text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in text:
    print(f" Добрый день, {i.split()[-1].title()}!")