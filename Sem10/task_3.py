"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

my_list = [bytes('attribute', 'utf-8'), bytes('класс', 'utf-8'),
           bytes('функция', 'utf-8'), bytes('type', 'utf-8')]
for line in my_list:
    print(line)