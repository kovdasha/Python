#Пользователь вводит строку из нескольких слов,
#разделённых пробелами. Вывести каждое слово с новой строки.
#Строки необходимо пронумеровать. Если слово длинное,
#выводить только первые 10 букв в слове.

input_string = input("Введите список слов через пробел: ").split()
for i in range(len(input_string)):
    print(f"{i + 1}. {input_string[i][:10]}")