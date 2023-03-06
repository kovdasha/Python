#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = int(input("Введите число: "))
degree = 2
while degree <= n:
    print(f"{degree} ")
    degree = degree * 2