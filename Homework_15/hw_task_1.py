"""Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование."""
import os
from collections import namedtuple
import logging
import argparse

logging.basicConfig(format='%(msg)s', filename='log.csv', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def walk_dir(dir_):
    lst = []
    args = 'name,extension,dir_flag,parent_name'
    FileObject = namedtuple('FileObject', args)
    logger.info(args)
    for path, *_ in os.walk(dir_):
        for item in os.listdir(path):
            name_ext = item.strip('.').split('.')
            name = name_ext[0]
            extension = name_ext[1] if len(name_ext) == 2 else None
            dir_flag = os.path.isdir(os.path.join(path, item))
            parent_name = os.path.basename(path)
            obj = FileObject(name, extension, dir_flag, parent_name)
            lst.append(obj)
            logger.info('{},{},{},{}'.format(*obj))
    return lst


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser to walk directory script')
    parser.add_argument('path', metavar='path', help='Directory path to walk')
    args = parser.parse_args()
    walk_dir(args.path)
