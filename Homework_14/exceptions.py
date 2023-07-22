class MyException(Exception):
    pass


class AccessException(MyException):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f'Ошибка доступа! ' \
               f'Пользователь с ID = {self.user_id} нет в списке пользователей..'


class LevelException(MyException):
    def __init__(self, admin_level, user_level, act):
        self.admin_level = admin_level
        self.user_level = user_level
        self.act = act

    def __str__(self):
        return f'Ошибка уровня! ' \
               f'Пользователь с уровнем {self.admin_level} не может {self.act}' \
               f' пользователя с уровнем {self.user_level}.'
