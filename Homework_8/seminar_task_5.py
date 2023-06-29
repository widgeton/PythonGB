"""Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import json
import pickle
import os


def func(dir_):
    json_files = [file for file in os.listdir(dir_) if file.endswith('.json')]
    for json_file in json_files:
        with (open(os.path.join(dir_, json_file), 'r', encoding='utf-8') as json_f,
              open(os.path.join(dir_, json_file.split('.')[0] + '.pickle'), 'wb') as pickle_f):
            pickle.dump(json.load(json_f), pickle_f)


if __name__ == '__main__':
    func(os.getcwd())
    with open('data.pickle', 'rb') as f:
        print(pickle.load(f))
