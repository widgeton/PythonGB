"""✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def get_sum_between(lst: list[int], idx_1: int, idx_2: int):
    if idx_1 < 0:
        if len(lst) + idx_1 < 0:
            idx_1 = 0
        else:
            idx_1 = len(lst) + idx_1

    if idx_2 < 0:
        if len(lst) + idx_2 < 0:
            idx_2 = 0
        else:
            idx_2 = len(lst) + idx_2

    return sum(lst[min(idx_1, idx_2):max(idx_1, idx_2)])


if __name__ == '__main__':
    nums = [5, 7, 10, -6, 9, 0, 5, 1, 54]
    print(get_sum_between(nums, 2, -3))
