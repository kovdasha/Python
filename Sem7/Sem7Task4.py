#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
#(метод init()), который должен принимать данные (список списков) для
#формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в
#виде прямоугольной схемы.
#Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
#привычном виде.
#Далее реализовать перегрузку метода add() для реализации операции сложения двух
#объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
#матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
#первой строки первой матрицы складываем с первым элементом первой строки второй
#матрицы и т.д.

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, second_matrix):
        if len(self.matrix) != len(second_matrix.matrix):
            return None
        result = []
        for item in zip(self.matrix, second_matrix.matrix):
            result.append([sum([i, j]) for i, j in zip(*item)])

        return Matrix(result)

m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [[3, 5, 8], [3, 8, 3], [7, 1, 1]]
matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)

print(matrix_1)
print()
print(matrix_2)
print('Новая матрица:')
print(matrix_1 + matrix_2)
