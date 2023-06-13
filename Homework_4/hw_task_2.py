""" Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""
import typing as tp


def func(*, a, b, c):
    return {value if isinstance(value, tp.Hashable) else str(value): key for key, value in locals().items()}


if __name__ == '__main__':
    print(func(a='qwerty', b=[1, 2, 3], c=8))
