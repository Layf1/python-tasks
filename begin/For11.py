#Дано целое число N (> 0).
#Найти сумму N² + (N + 1)² + (N + 2)² + ... + (2·N)².
n = int(input())
total = 0.0
for i in range(1, n + 1):
    total += (1 + i) ** 2
print(total)