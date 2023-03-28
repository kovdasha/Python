"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']

for line in my_list:
    in_bytes = line.encode("utf-8")
    print(f"тип: {type(in_bytes)}, содержание:  {in_bytes}")

    in_str = in_bytes.decode("utf-8")
    print(f"тип: {type(in_str)}, содержание:  {in_str}")