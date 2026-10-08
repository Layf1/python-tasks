#Даны переменные A, B, C.
#Изменить их значения, переместив содержимое A в B,B — в C, C — в A, и вывести новые значения переменных A, B, C.
a = float(input())
b = float(input())
c = float(input())
temp = a
a = b
b = temp
mpet = b
b = c
c = mpet
mept = c
c = a
a = mept
print(a)
print(b)
print(c)