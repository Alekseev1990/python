"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time
from colorama import init


class TrafficLights:
    __color_red = "red"
    __color_yellow = "yellow"
    __color_green = "green"

    #  метод
    def running(self, color_red, color_yellow, color_green):
        self.__color_red = color_red
        print("сигнал светофора:" + '\033[31m' + f' {self.__color_red}')
        time.sleep(7)
        self.__color_yellow = color_yellow
        print('\033[39m' + "сигнал светофора:" + '\033[33m' + f' {self.__color_yellow}')
        time.sleep(2)
        self.__color_green = color_green
        print('\033[39m' + "сигнал светофора:" + '\033[1m\033[32m' + f' {self.__color_green}')
        time.sleep(7)


a = TrafficLights()
a.running("red", "yellow", "green")


# class TrafficLights:
#     __color = "color"
#
#     #  метод
#     def running(self):
#         print('\033[39m' + "сигнал светофора:" + '\033[31m' + " red")
#         time.sleep(7)
#         print('\033[39m' + "сигнал светофора:" + '\033[33m' + " yellow")
#         time.sleep(2)
#         print('\033[39m' + "сигнал светофора:" + '\033[32m' + " green")
#         time.sleep(7)
#
#
# a = TrafficLights()
# a.running()
