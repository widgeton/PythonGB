"""
✔ Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
✔ *Верните все возможные варианты комплектации рюкзака.

Решение задачи с использованием модуля itertools.
"""
import itertools as itr


def is_valid(lst: tuple, things: dict[str: int], payload: int) -> bool:
    """Проверяет вес набора на перевес и возможность добавления вещей в набор без перевеса."""
    weight = 0
    for item in lst:
        weight += things[item]

    if weight > payload:
        return False
    for key in things:
        if key not in lst and weight + things[key] <= payload:
            return False
    return True


def get_sets(things: dict[str: int], payload: int) -> list[tuple]:
    sets = []
    for i in range(1, len(things)):
        for set_ in itr.combinations(things.keys(), i):
            if is_valid(set_, things, payload):
                sets.append(set_)
    return sets


if __name__ == '__main__':
    things = {'tent': 5, 'match': 1, 'knife': 2, 'sleepbag': 3, 'mug': 2, 'bowl': 2,
              'spoon': 1, 'food': 3, 'water': 4, 'kettle': 4, 'axe': 5}
    payload = 11
    print(*get_sets(things, payload), sep='\n')
