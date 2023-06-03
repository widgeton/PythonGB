# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

i = 2
first_row = ''
second_row = ''
while i <= 10:
    first_row += f'2 x {i:<2d}= {2 * i:>2d}\t\t' \
                 f'3 x {i:<2d}= {3 * i:>2d}\t\t' \
                 f'4 x {i:<2d}= {4 * i:>2d}\t\t' \
                 f'5 x {i:<2d}= {5 * i:>2d}\n'
    second_row += f'6 x {i:<2d}= {6 * i:>2d}\t\t' \
                  f'7 x {i:<2d}= {7 * i:>2d}\t\t' \
                  f'8 x {i:<2d}= {8 * i:>2d}\t\t' \
                  f'9 x {i:<2d}= {6 * i:>2d}\n'
    i += 1

print(first_row, second_row, sep='\n')
