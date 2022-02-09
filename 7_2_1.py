"""
(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе
«руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""


import os

folders = [["settings",  [
                ["--__init__.py", []],
                ["--dev.py",      []],
                ["--dev.py",      []],
                ["--prod.py",     []]]],
          ["mainnapp",  [
                ["--__init__.py", []],
                ["--models.py",   []],
                ["--views.py",    []],
                ["--templates",   []]]],
          ["authapp",   [
                ["--__init__.py", []],
                ["--models.py",   []],
                ["--views.py",    []],
                ["--templates",   []]]]]


def exist(way):
    if not os.path.exists(path):  # если путь не существует
        os.mkdir(fullpath)  # создать путь


def new_folder(root, data):
    if data:  # если не пустые данные
        for d in data:   # запускаю цикл по элементам
            name = d[0]  # имя 0 элемент
            os.path.join(root, name)  # собираю полный путь
            exist(path)  # запуск функции. если путь не существует, создать его
            new_folder(path, d[1])


path = r"C:\Users\Alex\Desktop\Домашка"
project_name = "project_7_2_1"
fullpath = os.path.join(path, project_name)
exist(fullpath)  # создаем папку project_name то есть project_7_2_1

new_folder(fullpath, folders)
