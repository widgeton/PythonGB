"""
✔ Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
✔ *Верните все возможные варианты комплектации рюкзака.
"""

PAYLOAD = 11
things = {'tent': 5, 'match': 1, 'knife': 2, 'sleepbag': 3, 'mug': 2, 'bowl': 2,
          'spoon': 1, 'food': 3, 'water': 4, 'kettle': 4, 'axe': 5}

sets_of_things = set()
for thing in things:
    set_of_things = [thing]
    weight_of_set = things[thing]
    for other in things:
        if other != thing and things[other] <= PAYLOAD - weight_of_set:
            set_of_things.append(other)
            weight_of_set += things[other]
    sets_of_things.add(frozenset(set_of_things))

print('Наборы вещей:')
for item in sets_of_things:
    print(*item, sep=', ')
