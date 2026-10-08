#Даны три целых числа. 
# Найти количество положительных чисел в исходном наборе.
A = int(input())
B = int(input())
C = int(input())
count = (A > 0) + (B > 0) + (C > 0)
print(count)