"""Создайте функцию генератор чисел Фибоначчи"""


def fibonacci(n: int):
    penult, last = 0, 1
    if n > 0:
        yield penult
    if n > 1:
        yield last
    while n > 2:
        penult, last = last, penult + last
        n -= 1
        yield last


if __name__ == '__main__':
    print(*fibonacci(6))
