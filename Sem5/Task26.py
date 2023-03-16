#Напишите программу, которая на вход принимает два числа A и B,
#и возводит число А в целую степень B с помощью рекурсии.

def degree_of_number(number, degree, result=1.0):
    if degree == 0:
        return result
    elif degree > 0:
        result = result * number
        return degree_of_number(number, degree - 1, result)
    elif degree < 0:
        result = result / number
        return degree_of_number(number, degree + 1, result)

input_number = int(input("Введите число А: "))
input_degree = int(input("Введите число В: "))
print("Результат возведения числа А в степень В: ", degree_of_number(input_number, input_degree))