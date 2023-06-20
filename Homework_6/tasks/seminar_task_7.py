"""Задача 7. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
   Домашняя задача 1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей
даты на проверку.
"""
from sys import argv

__all__ = ['may_exist']


def _is_leap(year):
    return year % 4 == 0 or year % 100 != 0 and year % 400 == 0


def may_exist(date):
    day, month, year = (int(item) for item in date.split('.'))
    if not 0 < day < 32 or not 0 < month < 13 or not 0 < year < 10_000:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and _is_leap(year) and day > 29:
        return False
    if month == 2 and not _is_leap(year) and day > 28:
        return False
    return True


if __name__ == '__main__':
    print(may_exist(argv[1]))
