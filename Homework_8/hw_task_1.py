"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий
размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import json
import csv
import pickle
import os


def get_dir_size(dir_):
    size = 0
    for path, _, files in os.walk(dir_):
        for file in files:
            size += os.path.getsize(os.path.join(path, file))
    return size


def func(dir_=os.getcwd(), json_file='data_dir.json', csv_file='data_dir.csv', pickle_file='data_dir.pickle'):
    dicts = []
    for path, *_ in os.walk(dir_):
        parent = os.path.basename(path)
        for item in os.listdir(path):
            abs_path = os.path.join(path, item)
            if os.path.isdir(abs_path):
                type_ = 'directory'
                size = get_dir_size(abs_path)
            else:
                type_ = 'file'
                size = os.path.getsize(abs_path)
            dicts.append({'name': item, 'parent': parent, 'type': type_, 'size': size})

    with (open(json_file, 'w', encoding='utf-8') as json_f,
          open(csv_file, 'w', encoding='utf-8', newline='') as csv_f,
          open(pickle_file, 'wb') as pickle_f):
        json.dump(dicts, json_f, indent=2)
        pickle.dump(dicts, pickle_f)
        writer = csv.DictWriter(csv_f, fieldnames=dicts[0])
        writer.writeheader()
        writer.writerows(dicts)


if __name__ == '__main__':
    func()
