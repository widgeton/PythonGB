"""Задание 5.Создайте три (или более) отдельных классов животных. Например: рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
   Задание 6. Доработайте задачу 5. Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    up_limb = 2

    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span

    def get_wing_len(self):
        """Возвращает длину одного крыла"""
        return self.wing_span / self.up_limb


class Fish(Animal):
    light_coef = 0.015

    def __init__(self, name, dwell_depth):
        super().__init__(name)
        self.dwell_depth = dwell_depth

    def get_light_level(self):
        """Возвращает уровень освещенности на глубине обитания"""
        light_level = 1 - self.dwell_depth * self.light_coef
        if light_level < 0:
            return 0
        return light_level


class Insect(Animal):
    def __init__(self, name, larva_term):
        super().__init__(name)
        self.larva_term = larva_term

    def get_left_time(self, time):
        """Возвращает оставшееся время созревание личинки насекомого"""
        rest_time = self.larva_term - time
        if rest_time < 0:
            return 0
        return rest_time

