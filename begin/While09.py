# While9. Дано N (> 1). Найти наименьшее K, при котором 3^K > N.
n = int(input())
power = 1   
k = 0
while power <= n:
    power *= 3
    k += 1
print(k)