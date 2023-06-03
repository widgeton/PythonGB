"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки."""
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

TRY_LIMIT = 10
counter = 0
while counter <= TRY_LIMIT:
    counter += 1
    guess_num = int(input(f'Попытка № {counter}. Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if guess_num == num:
        print('Вы угадали!')
        break
    elif guess_num < num:
        print('Вы не угадали. Загаданное число БОЛЬШЕ введенного.')
    elif guess_num > num:
        print('Вы не угадали. Загаданное число МЕНЬШЕ введенного.')

else:
    print(f'Вы потратили все попытки. Загаданное число: {num}')
