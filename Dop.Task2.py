# Найдите сумму цифр трехзначного числа.

number = input("Введите трехзначное число: ")
number = int(number)
num1 = number // 100
num2 = (number // 10) % 10
num3 = number % 10
print(f"Сумма цифр трехзначного числа = {num1 + num2 + num3}")