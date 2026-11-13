#Дано вещественное число A и целое число N (> 0).
#Найти A в степени N: A N = A · A · ... · A (число A перемножается N раз).
A = float(input())
N = int(input())

result = 1.0

for i in range (N):
    result *= A

print(result)