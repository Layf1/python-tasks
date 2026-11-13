#Даны переменные A, B, C.
#Изменить их значения, переместив содержимое A в C, C — в B, B — в A, и вывести новые значения переменных A, B, C.
a = int(input())
b = int(input())
c = int(input())
temp = a
a = c
c = temp
pmet = c
c = b
b =  pmet
mpte = b
b = a
a = mpte
print(a)
print(b)
print(c)