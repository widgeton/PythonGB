"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV."""
import csv
import json


def func(csv_file, json_file):
    with (open(csv_file, 'w', encoding='utf-8', newline='') as csv_f,
          open(json_file, 'r', encoding='utf-8') as json_f):
        dcts = json.load(json_f)
        lst = []
        for access, dct in dcts.items():
            for id_, name in dct.items():
                lst.append([id_, name, access])
        writer = csv.writer(csv_f)
        writer.writerow(['id', 'name', 'access'])
        writer.writerows(lst)


if __name__ == '__main__':
    func('data.csv', 'data.json')
