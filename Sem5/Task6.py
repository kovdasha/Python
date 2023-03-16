#В программе генерируется случайное целое число от 0 до 100.
#Пользователь должен его отгадать не более чем за 10 попыток. После каждой
#неудачной попытки должно сообщаться больше или меньше введенное пользователем
#число, чем то, что загадано. Если за 10 попыток число не отгадано,
#то вывести загаданное число.
#Решите через рекурсию. В задании нельзя применять циклы.

import random
def guess_number(number, count=0):
    if count == 10:
        print(f'Вы не угадали! Было загадано число {number}')
    else:
        input_number = int(input('Введите число от 0 до 100: '))
        if input_number == number:
            print(f'Вы угадали! Поздравляю!')
            return
        elif number > input_number:
            print('Загаданное число больше')
        elif number < input_number:
            print('Загаданное число меньше')
        guess_number(number, count + 1)


random_number = random.randint(0, 100)
guess_number(random_number)