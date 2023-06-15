"""Напишите функцию для транспонирования матрицы"""


def transpose_matrix(matrix: list[list]):
    return [*map(list, zip(*matrix))]


if __name__ == '__main__':
    m = [
        [2, 5, 7, 9],
        [6, 8, 10, 7],
        [1, 5, 9, 0],
    ]
    for row in m:
        print(row)
    print()
    for row in transpose_matrix(m):
        print(row)
