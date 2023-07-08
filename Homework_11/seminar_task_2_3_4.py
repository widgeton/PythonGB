"""Задание 2. Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее созданных экземпляров
сохраняются в пару списков-архивов. list-архивы также являются свойствами экземпляра.
   Задание 3. Добавить строки документации для классов.
   Задание 4. Добавьте методы представления экземпляра для программиста и для пользователя.
"""


class Archive:
    """Класс Архив, который хранит параметры всех его созданных объектов"""
    _nums = []
    _strings = []

    def __init__(self, num: int | float, string: str):
        self.num = num
        self.string = string
        self._nums.append(num)
        self._strings.append(string)

    def __str__(self):
        return f'{self.num}, {self.string}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.num}, "{self.string}")'
