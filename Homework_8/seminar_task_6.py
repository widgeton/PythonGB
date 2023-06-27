"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара. Функция должна извлекать
ключи словаря для заголовков столбца из переданного файла.
"""
import pickle
import csv


def func(pickle_file, csv_file):
    with (open(pickle_file, 'rb') as pickle_f,
          open(csv_file, 'w', encoding='utf-8', newline='') as csv_f):
        dicts = pickle.load(pickle_f)
        dct_writer = csv.DictWriter(csv_f, fieldnames=dicts[0])
        dct_writer.writeheader()
        dct_writer.writerows(dicts)


if __name__ == '__main__':
    func('users.pickle', 'users2.csv')
