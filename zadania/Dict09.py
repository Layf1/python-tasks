# Dict9. Построить словари из N и M пар. Слить второй в первый через update.
# Вывести размер результата и значение ключа, который был в обоих словарях
# (такой ключ гарантированно есть).

n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value

m = int(input())
d2 = {}
shared_key = None
for i in range(m):
    key = input()
    value = int(input())
    if key in d1:
        shared_key = key
    d2[key] = value

d1.update(d2)
print(len(d1))
print(d1[shared_key])