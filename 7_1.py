"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os


# path = r"C:\Users\Alex\Desktop\Домашка"
# root = 'my_project_7_1'
# folders = ["settings", "mainnapp", "adminapp", "authapp"]
# for folder in folders:
#     if not os.path.exists("my_project"):
#         os.makedirs(os.path.join(root, folder))


folder_list = {"my_project": [{"settings": []}, {"maimapp": []}, {"adminapp": []}, {"authapp": []}]}

for key, value in folder_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
