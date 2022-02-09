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

path = r"C:\Users\Alex\Desktop\Домашка"
project_name = "project_7_2"
folders = [["settings",  [
                ["--__init__.py", []],
                ["--dev.py",      []],
                ["--prod.py",     []]]],
          ["mainnapp",  [
                ["--__init__.py", []],
                ["--models.py",   []],
                ["--views.py",    []],
                ["--templates",   [
                    ["--mainapp", [
                        ["--base.html", []],
                        ["--index.html", []],
                    ]],
                ]]]],
          ["authapp",   [
                ["--__init__.py", []],
                ["--models.py",   []],
                ["--views.py",    []],
                ["--templates",   [
                    ["--authapp",[
                        ["--base.html" ,[]],
                        ["--index.html" ,[]],
                    ]],
                ]]]]]


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def build(root, data):
    if data:  # если не пустые данные
        for d in data:  # запускаю цикл по элементам
            name = d[0]  # имя 0 элемент
            path = os.path.join(root, name)  # собираю полный путь
            create_folder(path)   # запуск функции. если путь не существует, создать его
            build(path, d[1])  # рекурсия на уровень глубже. обязательно в конце уровня должен быть пустой элемент


fullpath = os.path.join(path, project_name)
create_folder(fullpath)
#
# for f in folders:
#     folder = os.path.join(fullpath, f)
#     create_folder(folder)

build(fullpath, folders)
