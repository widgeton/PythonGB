# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

i = 2
first_row = ''
second_row = ''
while i <= 10:
    first_row += f'2 x {i} = {2 * i}\t\t' \
                 f'3 x {i} = {3 * i}\t\t' \
                 f'4 x {i} = {4 * i}\t\t' \
                 f'5 x {i} = {5 * i}\n'
    second_row += f'6 x {i} = {6 * i}\t\t' \
                  f'7 x {i} = {7 * i}\t\t' \
                  f'8 x {i} = {8 * i}\t\t' \
                  f'9 x {i} = {6 * i}\n'
    i += 1

print(first_row, second_row, sep='\n')
