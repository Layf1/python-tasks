# Dict7. Построить словарь из N пар. Вывести ключ с наибольшим значением
# (перебор с кандидатом; значения различны).

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

best_key = None
for key in d:
    if best_key is None or d[key] > d[best_key]:
        best_key = key

print(best_key)