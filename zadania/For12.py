#Дано целое число N (> 0).
#Найти произведение 1.1 · 1.2 · 1.3 · ... (N     сомножителей).
n = int(input())
total = 1
for i in range(1, n + 1):
    i = 1 + i * 0.1
    total = total * i
print(total)