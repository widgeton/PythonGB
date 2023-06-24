"""✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def write_names_and_nums(names, nums):
    with (open(names, 'r', encoding='utf-8') as names_f,
          open(nums, 'r', encoding='utf-8') as nums_f,
          open('names_and_nums.txt', 'w', encoding='utf-8') as names_and_nums):
        nums = list(nums_f)
        names = list(names_f)
        while len(nums) != len(names):
            if len(nums) > len(names):
                names += names[:len(nums) - len(names)]
            else:
                nums += nums[:len(names) - len(nums)]

        for num, name in zip(nums, names):
            a, b = map(float, num[:-1].split('|'))
            mul = a * b
            if mul < 0:
                names_and_nums.write(f'{name[:-1].lower()} {-mul}\n')
            else:
                names_and_nums.write(f'{name[:-1].upper()} {round(mul)}\n')


if __name__ == '__main__':
    write_names_and_nums('names.txt', 'nums.txt')
