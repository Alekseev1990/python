"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""

from random import choice


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Transport speed {speed}, color {color}, {name}, is police? {is_police}")

    direction = ["повернула направо", "повернула налево"]

    def show_speed(self):
        return f'Ваша скорость {self.speed} км/ч'

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn(self):
        return f"{self.name} {choice(self.direction)}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60}')
        else:
            print(f'Ваша скорость {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40}')
        else:
            print(f'Ваша скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    """Sport car"""


workcar = WorkCar(90, "черный", "поливалка")
towncar = TownCar(150, "white", "jeep")
sportcar = SportCar(120, "red", "ferrari")
policecar = PoliceCar(50, "black", "sheriff")

carlist = [workcar, towncar, sportcar, policecar]
# print(carlist)
for i in carlist:
    print(i.turn())
    print(i.stop())
    print(i.show_speed())
