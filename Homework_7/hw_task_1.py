"""Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов.
* При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extension>
"""
import os


def rename_group(new_name, old_ext, new_ext, dir_=os.getcwd()):
    if os.path.isdir(dir_):
        files = [file for file in os.listdir(dir_) if
                 os.path.isfile(os.path.join(dir_, file)) and
                 file.endswith(f'.{old_ext}')]

        for i, file in enumerate(files, 1):
            os.rename(os.path.join(dir_, file), os.path.join(dir_, f'{file.split(".")[0]}_{new_name}_{i}.{new_ext}'))


if __name__ == '__main__':
    rename_group('file', 'png', 'jpg', 'Fold')
