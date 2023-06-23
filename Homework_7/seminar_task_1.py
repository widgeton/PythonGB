"""Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""
import random as rnd


def fill_file(num, filename, min_=-1000, max_=1000):
    with open(filename, 'a', encoding='utf-8') as file:
        for i in range(num):
            file.write(f'{rnd.randint(min_, max_)}|{rnd.uniform(min_, max_)}\n')


if __name__ == '__main__':
    fill_file(5, 'nums.txt')
