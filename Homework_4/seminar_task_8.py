"""✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def func():
    dct = globals()
    for key in [*dct.keys()]:
        if key.endswith('s') and len(key) > 1:
            dct[key.rstrip('s')], dct[key] = dct[key], None


if __name__ == '__main__':
    s = 5
    nums = [7, 8, 9]
    literals = ['a', 'b', 'c']
    figure = 'square'

    print(f'{s = }\n{nums = }\n{literals = }\n{figure = }\n')
    func()
    print(f'{s = }\n{nums = }\n{literals = }\n{figure = }\n')
    print(f'{s = }\n{num = }\n{literal = }\n{figure = }\n')
