"""Задание 1. Создайте класс Моя Строка, где: будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
   Домашнее задание 1. Добавить строки документации и методы вывода.
"""
import datetime


class MyString(str):
    """Класс строки, которая хранит имя создателя и время создания"""

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.creating_time = datetime.datetime.now().time()
        return instance

    def __str__(self):
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}("{self}", "{self.author}")'
