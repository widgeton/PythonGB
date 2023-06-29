"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и
произведением чисел. Напишите функцию, которая создаёт из созданного ранее файла новый с данными
в формате JSON. Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки
"""
import json


def func(file, json_file):
    with (open(file, 'r', encoding='utf-8') as f,
          open(json_file, 'w', encoding='utf-8') as json_f):
        dct = {}
        for line in f:
            name, num = line.split()
            dct[name.capitalize()] = num.strip()

        json.dump(dct, json_f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    func('names_and_nums.txt', 'names_and_nums.json')
