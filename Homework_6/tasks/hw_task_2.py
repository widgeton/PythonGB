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
    for item_i in kit:
        for item_j in kit:
            x, y = abs(item_j[0] - item_i[0]), abs(item_j[1] - item_i[1])
            if not (x and y and x - y) and item_j != item_i:
                return False
    return True


def get_random_set_of_queens():
    queens = set()
    N = 8
    while len(queens) < N:
        queens.add((rnd.randint(0, N - 1), rnd.randint(0, N - 1)))
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
