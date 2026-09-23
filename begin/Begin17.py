#Даны три точки A, B, C на числовой оси.
#Найти длины отрезков AC и BC и их сумму.   
A = float(input())
B = float(input())
C = float(input())
AC = abs(C - A)
BC = abs(C - B)
summ = AC + BC