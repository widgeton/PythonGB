import json
import os.path


class User:
    def __init__(self, id_, name, access=None):
        self.id_ = id_
        self.name = name
        self.access = access

    def __eq__(self, other):
        return self.id_ == other.id_ and self.name == other.name


def set_users_in_json(json_file):
    if os.path.isfile(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {str(i): {} for i in range(1, 7 + 1)}

    while True:
        data = input('Введите через пробел имя, ID, уровень доступа от 1 до 7: ')
        if not data:
            break
        name, id_, access = data.split()
        for item in dct.values():
            if id_ in item and item[id_] != name:
                print('Это ID имеет другое имя пользователя!')
                break
        else:
            dct[access][id_] = name

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(dct, f, indent=2, ensure_ascii=False)
