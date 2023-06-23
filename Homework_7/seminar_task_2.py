"""✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
import random as rnd

LITERALS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
VOWELS = 'аеёиоуыэюя'


def write_names(num, name, min_=4, max_=7):
    with open(name, 'w', encoding='utf-8') as file:
        for _ in range(num):
            name = rnd.sample(LITERALS, rnd.randint(min_, max_))
            if not set(name) & set(VOWELS):
                half = len(name) // 2
                name = name[:half] + rnd.sample(VOWELS, half)
                rnd.shuffle(name)
            name = ''.join(name).capitalize()
            file.write(f'{name}\n')


if __name__ == '__main__':
    write_names(15, 'names.txt')
