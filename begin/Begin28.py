#Дано число A.
#Вычислить A¹⁵, используя две вспомогательные переменные и пять операций умножения. 
#Для этого последовательно находить A², A³, A⁵, A¹⁰, A¹⁵. 
#Вывести все найденные степени числа A.
A = float(input())
kvadro = A ** 2
triple = A ** 3
A2 = kvadro * 1
A3 = triple * 1
A5 = kvadro * triple
A10 = A5 ** 2
A15 = A10 * A5
print(A2)
print(A3)
print(A5)
print(A10)
print(A15)