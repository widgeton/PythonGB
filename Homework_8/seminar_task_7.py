"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle


def func(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        lsts = [*csv.reader(file)]
        print(pickle.dumps([{key: value for key, value in zip(lsts[0], lst)} for lst in lsts[1:]]))


if __name__ == '__main__':
    func('users2.csv')
