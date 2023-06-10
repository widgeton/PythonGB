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


def get_sets(current: list, remain: list, dct: dict, sets_lst: list, weight=0):
    """
    Функция рекурсивно получает все возможные вещевые наборы, которые весят не более PAYLOAD.
    """
    for thing in remain:
        if weight + dct[thing] > PAYLOAD:
            return frozenset(current)
        lst_1 = current.copy()
        lst_2 = remain.copy()
        lst_1.append(thing)
        lst_2.remove(thing)
        w = dct[thing] + weight
        res = get_sets(lst_1, lst_2, dct, sets_lst, w)
        if res is not None:
            sets_lst.append(res)


# Чтобы функция отработала правильно нужно передать ей список вещей
# отсортированные по весу в порядке возрастания.
things = dict(sorted(things.items(), key=lambda item: item[1]))

kits = []
get_sets([], [*things.keys()], things, kits)
kits = [*set(kits)]

# Избавляемся от наборов-подмножеств, в которые еще могли поместиться вещи.
i = 0
while i < len(kits):
    j = 0
    while j < len(kits):
        if kits[i] > kits[j]:
            kits.remove(kits[j])
            i = -1
            j -= 1
        j += 1
    i += 1

print('Возможные наборы вещей:')
for kit in kits:
    print(*kit, sep=', ')
