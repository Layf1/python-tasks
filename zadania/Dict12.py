# Dict12. Построить словарь из N пар с различными значениями.
# Построить обращённый словарь: значение -> ключ.
# Вывести его пары в порядке добавления исходного.

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

rev_d = {}
for key, value in d.items():
    rev_d[value] = key

for val, k in rev_d.items():
    print(f"{val}: {k}")