"""Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
Например, нельзя создавать прямоугольник со сторонами отрицательной длины."""
from abc import ABCMeta, abstractmethod


class MyException(Exception, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class NameException(MyException):
    _message = 'Ошибка имени! Имя должно начинаться с заглавной буквы и иметь только буквы.'

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self.name is None:
            return self._message
        return f'{self._message} Введенное имя: {self.name}'


class RangeException(MyException):
    _message = 'Значение не попало в диапазон!'

    def __init__(self, low_limit=float('-inf'), high_limit=float('inf')):
        self.low_limit = low_limit
        self.high_limit = high_limit

    def __str__(self):
        if self.low_limit != float('-inf') or self.high_limit != float('inf'):
            return f'{self._message} Оно должно быть в диапазоне от {self.low_limit} до {self.high_limit}.'
        return self._message


class MatrixException(MyException):
    _message = 'Ошибка матрицы!'

    def __init__(self, matrix=None):
        self.matrix = matrix

    def __str__(self):
        if self.matrix is None:
            return self._message
        str_matrix = "\n".join(map(str, self.matrix))
        return f'{self._message}\nВаша структура не является матрицей:\n{str_matrix}'


class MatrixOperationException(MyException):
    _message = 'Ошибка математической операции'

    def __init__(self, operation, matrix=None, matrix_to_add=None):
        self.operation = operation
        self.matrix = matrix
        self.matrix_to_add = matrix_to_add

    def __str__(self):
        if self.matrix is not None and self.matrix_to_add is not None:
            str_matrix = "\n".join(map(str, self.matrix))
            str_matrix_to_add = "\n".join(map(str, self.matrix_to_add))
            return f'{self._message}\nНевозможна операция {self.operation} с матрицей:\n{str_matrix}\n' \
                   f'И матрицей:\n{str_matrix_to_add}'

        if self.matrix_to_add is None and self.matrix is not None:
            str_matrix = "\n".join(map(str, self.matrix))
            return f'{self._message}\nНевозможна операция {self.operation} с матрицей:\n{str_matrix}'

        if self.matrix is None and self.matrix_to_add is not None:
            str_matrix_to_add = "\n".join(map(str, self.matrix_to_add))
            return f'{self._message}\nНевозможно операция {self.operation} с матрицей:\n{str_matrix_to_add}'

        return f'{self._message} {self.operation}!'


class AddMatrixException(MatrixOperationException):
    _operation = 'сложения'

    def __init__(self, matrix=None, matrix_to_add=None):
        super().__init__(self._operation, matrix, matrix_to_add)


class MulMatrixException(MatrixOperationException):
    _operation = 'умножения'

    def __init__(self, matrix=None, matrix_to_add=None):
        super().__init__(self._operation, matrix, matrix_to_add)
