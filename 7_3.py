"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в
родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
"""

import os
from os import walk, path, listdir
import shutil

project_name = "my_project"

try:
    for root, dirs, files in walk(project_name):  # перебор всего содержимого
        if "--templates" in dirs and root != project_name:  # если папка в my_project, но спрятана в папках
            for entry in listdir(path.join(root, "--templates")):  # выбираем путь к папке --templates
                shutil.copytree(path.join(root, "--templates", entry), path.join(project_name, "--templates", entry))
#  копируем древо папок после --templates
except FileExistsError:
    print("exist")
