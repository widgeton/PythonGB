"""Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. При перезапуске функции
уже записанные в файл данные должны сохраняться.
"""
import json
import os.path


def func(json_file):
    if os.path.isfile(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
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

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(dct, f)


if __name__ == '__main__':
    func('data.json')
