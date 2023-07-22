import json
from Homework_14.user import User
from Homework_14.exceptions import AccessException, LevelException


class Project:
    file_name = 'users.json'

    def __init__(self, users: list[User]):
        self._users = users
        self.admin: User = None

    @classmethod
    def from_json_file(cls, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            dct = json.load(f)

        lst = []
        for level, values in dct.items():
            for id_, name in values.items():
                lst.append(User(id_, name, level))

        return cls(lst)

    def login(self, id_, name):
        new_user = User(id_, name)
        for user in self._users:
            if user == new_user:
                self.admin = user
                break
        else:
            raise AccessException(id_)

    def add_user(self, id_, name, access):
        if self.admin.access > access:
            raise LevelException(self.admin.access, access, 'добавить')

        self._users.append(User(id_, name, access))

    def remove_user(self, id_):
        for user in self._users:
            if user.id_ == id_:
                break
        else:
            raise AccessException(id_)

        if self.admin.access > user.access:
            raise LevelException(self.admin.access, user.access, 'удалить')

        self._users.remove(user)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dicts = {str(i): {} for i in range(1, 7 + 1)}
        for user in self._users:
            dicts[user.access].update({user.id_: user.name})

        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(dicts, f, indent=2, ensure_ascii=False)

    def __contains__(self, item: User):
        for user in self._users:
            if user == item:
                return True
        return False

    def __eq__(self, other):
        if self.admin != other.admin:
            return False
        lst_self = sorted(self._users, key=lambda x: int(x.id_))
        lst_other = sorted(other._users, key=lambda x: int(x.id_))
        for item_self, item_other in zip(lst_self, lst_other):
            if item_self != item_other:
                return False
        return True
