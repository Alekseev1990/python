"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random


def get_jokes(n, repeat=True):
    """
    Функция возвращает случайные шутки в количестве n

    """

    list_of_jokes = []
    i = 0
    while i <= n:
        x = random.choice(["автомобиль", "лес", "огонь", "город", "дом"])  # Оптимизация
        y = random.choice(["сегодня", "вчера", "завтра", "позавчера", "ночью"])
        z = random.choice(["веселый", "яркий", "зеленый", "утопичный", "мягкий"])
        result = x + " " + y + " " + z
        list_of_jokes.append(result)
        unique = set(list_of_jokes) # блок удаления дублей
        unique_list = list(unique)
        i += 1
    print('\n'.join(sorted(unique_list)))  # \n для вывода в столбец, проверка, сортировка для проверки повторений,
# операция работает


get_jokes(200)


# from random import choice, rendrange
#
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#
# def get_jokes(n, repeat=False):
#     """
#     Функция возвращает случайную шутку
#
#     """
#
#     no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
#     list_of_j = []
#     list_min = min(no, adv, adj)
#
#     while n and len(list_min):
#         num = rendrange(len(list_min))
#         if repeat:
#             list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
#         else:
#             list_of_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
#         n += 1
#         return list_of_j
#
#
# get_jokes(20, True)