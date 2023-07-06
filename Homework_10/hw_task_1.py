"""Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""
from seminar_task_5_6 import Bird, Fish, Insect

TYPES = type[Bird, Fish, Insect]


class Factory:
    def __init__(self, class_name: TYPES, *args, **kwargs):
        self.class_name = class_name
        self.args = args
        self.kwargs = kwargs

    def get_object(self):
        return self.class_name(*self.args, **self.kwargs)
