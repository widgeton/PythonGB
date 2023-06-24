"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""
import os


def group(dct, dir_=os.getcwd()):
    if os.path.isdir(dir_):
        files = [file for file in os.listdir(dir_) if os.path.isfile(os.path.join(dir_, file))]
        for fold, exts in dct.items():
            fold = os.path.join(dir_, fold)
            if not os.path.isdir(fold):
                os.makedirs(fold)
            for file in files:
                if file.split('.')[1] in exts:
                    os.replace(os.path.join(dir_, file), os.path.join(fold, file))


if __name__ == '__main__':
    dct = {'Видео': ('mkv', 'avi', 'mp4'),
           'Изображение': ('png', 'jpg', 'jpeg'),
           'Текст': ('txt', 'bin'),
           }
    group(dct, 'Fold')
