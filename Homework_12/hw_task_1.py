"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""
import csv


class Subject:
    __low_mark = 2
    __high_mark = 5
    __low_test_result = 0
    __high_test_result = 100

    def __init__(self, name: str, mark: int, tests_results: list[int]):
        self._name = name
        self._tests_results = []
        self.tests_results = tests_results
        self.mark = mark

    @property
    def name(self):
        return self._name

    @property
    def tests_results(self):
        return self._tests_results

    @tests_results.setter
    def tests_results(self, value: list[int] | int):
        if isinstance(value, list):
            for res in value:
                self._check_value_in_range(res, self.__low_test_result, self.__high_test_result)
            self._tests_results.extend(value)
        else:
            self._check_value_in_range(value, self.__low_test_result, self.__high_test_result)
            self._tests_results.append(value)

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._check_value_in_range(value, self.__low_mark, self.__high_mark)
        self._mark = value

    @staticmethod
    def _check_value_in_range(value, start, stop):
        if not start <= value <= stop:
            raise ValueError(f'Значение должно быть в диапазоне от {start} до {stop}')


class Check:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value: str):
        if not value.isalpha() and value.istitle():
            raise ValueError('Имя должно начинаться с заглавной буквы и иметь только буквы')
        setattr(instance, self.name, value)


class Student:
    full_name = Check()

    def __init__(self, full_name, subjects_csv_file):
        self.full_name = full_name
        self._subjects = []
        self._set_subjects(subjects_csv_file)

    def _set_subjects(self, subjects_csv_file):
        with open(subjects_csv_file, 'r', encoding='utf-8', newline='') as file:
            for subject_name, mark, tests_results in [*csv.reader(file)][1:]:
                self._subjects.append(Subject(subject_name, int(mark), eval(tests_results)))

    @property
    def subjects(self):
        return self._subjects

    def get_avg_subject_tests_results(self, subject_name):
        for subject in self._subjects:
            if subject.name == subject_name:
                return sum(subject.tests_results) / len(subject.tests_results)

    def get_avg_mark(self):
        sum_ = 0
        for subject in self._subjects:
            sum_ += subject.mark
        return sum_ / len(self._subjects)


if __name__ == '__main__':
    student = Student('ИвановИван', 'student.csv')
    print(student.get_avg_mark())
    print(student.get_avg_subject_tests_results('Физика'))
