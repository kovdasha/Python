# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

n = input("Введите число n: ")
nn = n + n
nnn = n + n + n
print(int(n) + int(nn) + int(nnn))