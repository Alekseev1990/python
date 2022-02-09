"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""


with open('pars_logs.txt', 'w', encoding='utf-8') as d:  # создаем файл для записи новых данных
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:  # открываем исходный файл для чтения
        content = ((line.split()[0], line.split()[5][1:], line.split()[6])for line in f)
# сначала действие со строкой, выбираем 1 элемент, 6 элемент без одной ковычки, 7 элемент. Элементы разделены пробелом
        for i in content:
            print(i, file=d)
# циклом применяем условие ко всем строкам
# где with close не нужен
