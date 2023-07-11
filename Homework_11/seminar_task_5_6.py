"""Задание 5. Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры,
а не длину и ширину. При вычитании не допускайте отрицательных значений.
   Задание 6. Добавьте сравнение прямоугольников по площади. Должны работать все шесть операций сравнения.
   Домашнее задание 1. Добавить строки документации и методы вывода.
"""


class Rectangle:
    """Класс реализующий математические свойства прямоугольника"""

    def __init__(self, length, width=None):
        self.length = self.width = length
        if width is not None:
            self.width = width

    def __add__(self, other):
        new_perimeter = self.get_perimeter() + other.get_perimeter()
        min_side = min(self.length, self.width, other.length, other.width)
        return Rectangle(min_side, (new_perimeter - min_side * 2) / 2)

    def __sub__(self, other):
        new_perimeter = self.get_perimeter() - other.get_perimeter()
        side = new_perimeter / 4
        return Rectangle(side)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __ge__(self, other):
        return self.get_square() >= other.get_square()

    def __str__(self):
        return f'           {self.length}  \n' \
               f'   ------------------\n' \
               f'  |                  |\n' \
               f'{self.width} |                  |\n' \
               f'  |                  |\n' \
               f'   ------------------'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.length}, {self.width})'

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_square(self):
        return self.length * self.width
