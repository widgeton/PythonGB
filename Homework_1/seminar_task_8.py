# Нарисовать в консоли ёлку спросив у пользователя количество рядов

rows = int(input('Введите количество рядов елки: '))
stars = '*'
space = ' '
while rows > 0:
    rows -= 1
    print(space * rows + stars)
    stars += '**'
