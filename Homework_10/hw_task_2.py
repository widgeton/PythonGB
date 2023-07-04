"""Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра."""
import os
import json
import csv


class Serializer:
    def __init__(self, cwd=os.getcwd()):
        self.cwd = cwd

    def task_1_func(self, txt_file):
        file = os.path.join(self.cwd, txt_file)
        if os.path.exists(file):
            with (open(file, 'r', encoding='utf-8') as f,
                  open(file.rsplit('.', 1)[0] + '.json', 'w', encoding='utf-8') as json_f):
                dct = {}
                for line in f:
                    name, num = line.split()
                    dct[name.capitalize()] = num.strip()

                json.dump(dct, json_f, ensure_ascii=False, indent=2)

    def task_2_func(self, json_file):
        file = os.path.join(self.cwd, json_file)
        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as f:
                dct = json.load(f)
        else:
            dct = {str(i): {} for i in range(1, 7 + 1)}

        while True:
            data = input('Введите через пробел имя, ID, уровень доступа: ')
            if not data:
                break
            name, id_, access = data.split()
            if id_ not in dct[access]:
                dct[access][id_] = name

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(dct, f)

    def task_3_func(self, json_file):
        file = os.path.join(self.cwd, json_file)
        if os.path.exists(file):
            with (open(file.rsplit('.', 1)[0] + '.csv', 'w', encoding='utf-8', newline='') as csv_f,
                  open(file, 'r', encoding='utf-8') as json_f):
                dcts = json.load(json_f)
                lst = []
                for access, dct in dcts.items():
                    for id_, name in dct.items():
                        lst.append([id_, name, access])
                writer = csv.writer(csv_f)
                writer.writerow(['id', 'name', 'access'])
                writer.writerows(lst)
