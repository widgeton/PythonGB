"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def get_tuple(abs_path: str):
    path, filename = abs_path.rsplit('\\', 1)
    return path, *filename.split('.')


if __name__ == '__main__':
    p = 'C:\\Users\\user\\Documents\\picture.png'
    print(get_tuple(p))
