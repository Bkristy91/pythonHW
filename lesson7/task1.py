# Задание №1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__() ), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, ListOfList):
        self.ListOfList = ListOfList
        self.count_line_Matrix = len(ListOfList[0])
        self.count_column_Matrix = len(ListOfList)

    def __str__(self):
        sent = ''
        for line in self.ListOfList:
            for el in line:
                sent += str(el) + ' '
            sent += '\n'
        return sent

    def __add__(self, other):
        if self.count_column_Matrix == other.count_column_Matrix and self.count_line_Matrix == other.count_line_Matrix:
            new_Matrix = []
            for lineSelf, lineOther in zip(self.ListOfList, other.ListOfList):
                lineNew = []
                for el_sel, el_other in zip(lineSelf, lineOther):
                    lineNew.append(el_sel + el_other)
                new_Matrix.append(lineNew)
            return Matrix(new_Matrix)
        else:
            return 'Невозможно сложить матрицы, разный размер'


a = Matrix([[1, 2, 3], [1, 2, 3]])
b = Matrix([[4, 5, 6], [7, 8, 9]])
c = a + b
print(c)