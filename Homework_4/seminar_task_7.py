"""✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""


def are_profitable(companies: dict[str:list[int]]):
    return all(map(lambda x: sum(x) > 0, companies.values()))


if __name__ == '__main__':
    cmps = {'Камношифеко': [800, 756, -345, 98, 256, -483],
            'Бомбардини': [9076, -5008, 723, 546, 1002, -9, 87],
            'Част и Кипуч': [867, -598, 78, -357, -872, 53, 46],
            }
    print(are_profitable(cmps))
