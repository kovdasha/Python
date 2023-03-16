#Вывести на экран коды и символы таблицы ASCII, начиная с символа
#под номером 32 и заканчивая 127-м включительно.
#Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
#Решите через рекурсию. В задании нельзя применять циклы.
#Допускается исп-е встроенных ф-ций

def print_ascii(start=32, count=0):
    if start == 128:
        return
    else:
        if count < 10:
            print(start, chr(start), end=' ', sep=' - ')
            print_ascii(start + 1, count + 1)
        else:
            print()
            print_ascii(start, 0)

print_ascii()