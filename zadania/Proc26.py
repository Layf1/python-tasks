# Proc26. Функция is_power5(k) возвращает True, если k (> 0) — степень пятёрки.
# Найти количество таких в наборе из 10 чисел.

def is_power5(k):
    cur = k
    while cur % 5 == 0 and cur > 0:
        cur //= 5
    return cur == 1

count = 0
for i in range(10):
    k = int(input())
    if is_power5(k):
        count += 1
print(count)