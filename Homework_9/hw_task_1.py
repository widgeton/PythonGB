"""Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
import csv
import json
import os.path
import random as rnd


def take_args_from_file(csv_file):
    with open(csv_file, 'r', encoding='utf-8', newline='') as f:
        lst_args = [*csv.reader(f)]

    def deco(func):
        res_lst = []

        def wrapper():
            for args in lst_args:
                res_lst.append(func(*map(float, args)))
            return res_lst

        return wrapper

    return deco


def log(json_file):
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f_r:
            dicts = json.load(f_r)
    else:
        dicts = []

    def deco(func):
        def wrapper(*args, **kwargs):
            dicts.append({'args': (*args, *kwargs.values()), 'result': (*map(str, func(*args, **kwargs)),)})
            with open(json_file, 'w', encoding='utf-8') as f_w:
                json.dump(dicts, f_w, indent=2)

        return wrapper

    return deco


@log('log.json')
def get_roots_of_quadratic_equation(a, b, c) -> tuple[float | complex, float | complex] | tuple[float]:
    D = b ** 2 - 4 * a * c
    if D != 0:
        x1 = (- b + D ** 0.5) / 2 * a
        x2 = (- b - D ** 0.5) / 2 * a
        return x1, x2
    return -b / 2 * a,


def write_rnd_nums_in_csv(min_num, max_num, csv_file, lines=200):
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerows([rnd.randint(min_num, max_num) for _ in range(3)] for _ in range(lines))


if __name__ == '__main__':
    write_rnd_nums_in_csv(1, 10, 'args.csv')
    take_args_from_file('args.csv')(get_roots_of_quadratic_equation)()
