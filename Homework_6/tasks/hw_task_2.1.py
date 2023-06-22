"""Немного более быстрый рандомный поиск решений задачи с 8 ферзями,
но в нем необходимо знать количество решений.
"""
import random as rnd
from tqdm import tqdm
from hw_task_2 import is_right

SOLUTIONS = 92


def show_board(queens: set[tuple[int, int]]):
    for i in range(8):
        g = [' '] * 8
        for j in queens:
            if i == j[0]:
                g[j[1]] = 'Q'
        print(8 - i, '|' + '|'.join(g) + '|')
    print('   A B C D E F G H')


def get_almost_random_set_of_queen():
    """Функция собирает случайный набор ферзей, которые не угрожают друг другу по горизонтали и вертикали"""
    kit = set()
    while len(kit) < 8:
        row = rnd.randint(0, 7)
        while row in (i[0] for i in kit):
            row = rnd.randint(0, 7)

        column = rnd.randint(0, 7)
        while column in (i[1] for i in kit):
            column = rnd.randint(0, 7)

        kit.add((row, column))
    return frozenset(kit)


def get_all_solution():
    i = 0
    solutions = set()
    pbar = tqdm(total=SOLUTIONS, ncols=SOLUTIONS)
    while i < SOLUTIONS:
        queens = get_almost_random_set_of_queen()
        if is_right(queens) and queens not in solutions:
            i += 1
            pbar.update(1)
            solutions.add(queens)
    pbar.close()
    return solutions


if __name__ == '__main__':
    for i, item in enumerate(get_all_solution(), 1):
        print(i)
        show_board(item)
