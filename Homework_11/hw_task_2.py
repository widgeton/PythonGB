"""Создайте класс Матрица. Добавьте методы для:
вывода на печать, сравнения, сложения, умножения матриц.
"""


class Matrix:
    def __init__(self, matrix: list[list]):
        self.check_matrix(matrix)
        self.matrix = matrix

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return False
        for i in range(len(other.matrix)):
            for j in range(len(other.matrix[i])):
                if other.matrix[i][j] != self.matrix[i][j]:
                    return False
        return True

    def __gt__(self, other):
        return self.get_size() > other.get_size()

    def __ge__(self, other):
        return self.get_size() >= other.get_size()

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([[self_j + other.matrix[i][j] for j, self_j in enumerate(self_i)] for i, self_i in
                           enumerate(self.matrix)])
        raise ValueError

    def __mul__(self, other):
        if len(self.matrix) == len(other.matrix[0]) and len(self.matrix[0]) == len(other.matrix):
            lst = []
            for i in range(len(self.matrix)):
                inner_lst = []
                for j in range(len(other.matrix)):
                    sum_ = 0
                    for k in range(len(self.matrix[i])):
                        sum_ += other.matrix[k][j] * self.matrix[i][k]
                    inner_lst.append(sum_)
                lst.append(inner_lst)
            return Matrix(lst)

        raise ValueError

    def __str__(self):
        output = ''
        for row in self.matrix:
            output += f'{row}\n'
        return output

    def get_size(self):
        return len(self.matrix[0]) * len(self.matrix)

    @staticmethod
    def check_matrix(matrix):
        length = len(matrix[0])
        for row in matrix:
            if len(row) != length:
                raise ValueError
