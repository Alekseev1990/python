"""
1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
"""

def print_sep(sep):
    print(sep * 150)


# variant 1 при большом количестве выражений не использовать
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

print_sep('-')

# variant 2
results = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for i in results:
    print(type(i))


# print(isinstance(15 * 3, int))
# print(isinstance(15 / 3, float))
# print(isinstance(15 // 3, int))
# print(isinstance(15 ** 3, int))
