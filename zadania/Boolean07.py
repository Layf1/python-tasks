#Даны три целых числа: A, B, C.
#Проверить истинность высказывания: «Число B находится между числами A и C».
A = int(input())
B = int(input())
C = int(input())

print((A > B and B > C) or (C > B and B > A)) 