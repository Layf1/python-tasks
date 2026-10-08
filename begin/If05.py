#Даны три целых числа. 
#Найти количество положительных и количество отрицательных чисел в исходном наборе.
A = int(input())
B = int(input())
C = int(input())

bad_count = (A < 0) + (B < 0) + (C < 0)
good_count = (A > 0) + (B > 0) + (C > 0)
print("Положительных",good_count)
print("Отрицательных", bad_count)