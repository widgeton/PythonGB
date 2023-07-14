"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""
import csv
from Homework_13.hw_task_1 import RangeException, NameException


class Range:
    def __init__(self, low_limit, high_limit):
        self.low_limit = low_limit
        self.high_limit = high_limit

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value: int | list[int]):
        attr_value = getattr(instance, self.name)

        if isinstance(value, int):
            self.check_range(value)
        elif isinstance(value, list):
            for item in value:
                self.check_range(item)

        if isinstance(attr_value, list) and isinstance(value, int):
            attr_value.append(value)
            value = attr_value
        elif isinstance(attr_value, list) and isinstance(value, list):
            attr_value.extend(value)
            value = attr_value

        if isinstance(attr_value, int) and isinstance(value, list):
            raise ValueError("Этому полю нельзя присвоить значение типа 'list'")

        setattr(instance, self.name, value)

    def check_range(self, value):
        if not self.low_limit <= value <= self.high_limit:
            raise RangeException(self.low_limit, self.high_limit)


class Subject:
    tests_results = Range(0, 100)
    mark = Range(2, 5)

    def __init__(self, name: str, mark: int, tests_results: list[int]):
        self._name = name
        self.tests_results = tests_results
        self.mark = mark

    def __getattr__(self, item):
        return None

    def get_avg_tests_results(self):
        return sum(self.tests_results) / len(self.tests_results)


class Check:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, name: str):
        if not name.isalpha() and name.istitle():
            raise NameException(name)
        setattr(instance, self.name, name)


class Student:
    full_name = Check()

    def __init__(self, full_name, subjects_csv_file):
        self.full_name = full_name
        self._subjects = self._get_subjects_dict(subjects_csv_file)

    def _get_subjects_dict(self, subjects_csv_file):
        subjects_dict = {}
        with open(subjects_csv_file, 'r', encoding='utf-8', newline='') as file:
            for subject_name, mark, tests_results in [*csv.reader(file, delimiter=';')][1:]:
                subjects_dict[subject_name] = Subject(subject_name, int(mark), self.parse_list(tests_results))
        return subjects_dict

    @staticmethod
    def parse_list(line: str):
        return [*map(int, line.strip('[]').split(', '))]

    def get_subject_names(self):
        return [*self._subjects.keys()]

    def get_subject(self, subject_name):
        return self._subjects[subject_name]

    def get_avg_subject_tests_results(self, subject_name):
        return self._subjects[subject_name].get_avg_tests_results()

    def get_avg_mark(self):
        sum_ = 0
        for subject in self._subjects.values():
            sum_ += subject.mark
        return sum_ / len(self._subjects)


if __name__ == '__main__':
    student = Student('ИвановИван', 'student.csv')
    print(student.get_avg_mark())
    print(student.get_avg_subject_tests_results('Физика'))
