"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title="draw something"):
        self.title = title


    def draw(self):
        return "Начало отрисовки"


class Pen(Stationery):
    def draw(self):
        return "Отрисовка ручкой"


class Pencil(Stationery):
    def draw(self):
        return "Отрисовка карандашом"


class Handle(Stationery):
    def draw(self):
        return "Отрисовка маркером"


stationery = Stationery()
pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")
newlist = [stationery, pen, pencil, handle]

for i in newlist:
    print(i.draw())
