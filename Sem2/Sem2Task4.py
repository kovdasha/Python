#Для списка реализовать обмен значений соседних элементов,
#т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().

some_list = input("Введите список элементов: ").split()
n = 0
while n <= len(some_list) // 2:
    temp_el = some_list[n]
    some_list[n] = some_list[len(some_list) - n - 1]
    some_list[len(some_list) - n - 1] = temp_el
    n += 1
print(some_list)
