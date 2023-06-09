"""
 Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
 а значение — кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

dct = {'Dan': ('tent', 'match', 'knife', 'sleepbag', 'mug', 'bowl', 'spoon', 'food', 'water'),
       'John': ('kettle', 'match', 'knife', 'sleepbag', 'mug', 'spoon', 'bowl', 'water'),
       'Alex': ('match', 'axe', 'knife', 'sleepbag', 'mug', 'bowl', 'spoon', 'food'),
       'Leon': ('match', 'knife', 'sleepbag', 'mug', 'bowl', 'spoon', 'food', 'water'),
       }

first = list(dct.keys())[0]
taken_by_each = set(dct[first])
present_unique = set()
not_present_unique = set()
for key_i in dct:
    taken_by_each &= set(dct[key_i])

    present_unique_i = set(dct[key_i])
    not_present_unique_i = set()
    for key_j in dct:
        if key_j != key_i:
            present_unique_i &= set(dct[key_i]) - set(dct[key_j])
            not_present_unique_i ^= set(dct[key_j]) - set(dct[key_i])
    present_unique |= present_unique_i
    not_present_unique |= not_present_unique_i

not_present_unique -= present_unique

names = {}
for key in dct:
    things = not_present_unique - set(dct[key])
    if things:
        names[key] = things

print('Вещи которые взяли каждый из друзей:')
print(*taken_by_each, sep=', ')
print('Вещи присутствующие уникально у каждого друга:')
print(*present_unique, sep=', ')
print('Вещи уникально отсутствующие (есть у всех, кроме одного):')
for key in names:
    print(key, '-', end=' ')
    print(*names[key], sep=',')
