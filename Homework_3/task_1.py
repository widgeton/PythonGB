"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst = [1, 2, 3, 1, 2, 4, 4, 8, 9, 6, 7, 4, 8]
res = [i for i in set(lst) if lst.count(i) > 1]
print(res)
