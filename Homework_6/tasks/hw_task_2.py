"""Задание 2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий
задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа
получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга
верните истину, а если бьют - ложь.
   Задание 3. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
*Выведите все успешные варианты расстановок.
"""
import random as rnd
import itertools as itr


def is_right(kit: set[tuple[int, int]]):
    for item in kit:
        for i in range(1, 8):
            if (item[0], item[1] + i) in kit or (item[0], item[1] - i) in kit or \
                    (item[0] + i, item[1]) in kit or (item[0] - i, item[1]) in kit or \
                    (item[0] + i, item[1] + i) in kit or (item[0] - i, item[1] + i) in kit or \
                    (item[0] + i, item[1] - i) in kit or (item[0] - i, item[1] - i) in kit:
                return False
    return True


def get_random_set_of_queens():
    queens = set()
    while len(queens) < 8:
        queens.add((rnd.randint(0, 7), rnd.randint(0, 7)))
    return queens


def get_all_solutions():
    return [item for item in itr.combinations(itr.combinations_with_replacement(range(8), 2), 8) if is_right(item)]


if __name__ == '__main__':
    count = 4
    while count > 0:
        queens = get_random_set_of_queens()
        if is_right(queens):
            print(queens)
            count -= 1
