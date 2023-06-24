"""Задача 4. ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
   Задача 5. ✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
   Задача 6. ✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
import os
import random as rnd
import string


def create_files(ext, dir_path, num_of_files=42,
                 min_len_name=6, max_len_name=30,
                 min_num_bytes=256, max_num_bytes=4096):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    for _ in range(num_of_files):
        name = rnd.choices(string.ascii_lowercase, k=rnd.randint(min_len_name, max_len_name))
        bytes_ = rnd.choices(string.ascii_letters, k=rnd.randint(min_num_bytes, max_num_bytes))
        name = f'{"".join(name)}.{ext}'
        i = 1
        while name in os.listdir(dir_path):
            name = name.split('.')
            name[0] += f'_{i}'
            name = '.'.join(name)
            i += 1
        with open(f'{os.path.join(dir_path, name)}', 'wb') as file:
            file.write(''.join(bytes_).encode(encoding='utf-8'))


def create_dif_files(dir_path, **kwargs):
    for ext, num in kwargs.items():
        create_files(ext, dir_path, num_of_files=num)


if __name__ == '__main__':
    create_dif_files('Fold', txt=2, bin=4, png=8)
