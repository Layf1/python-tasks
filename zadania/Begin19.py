#Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2,y2). 
# Стороны прямоугольника параллельны осям координат.
#Найти периметр и площадь данного прямоугольника.
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
side = abs(x2 - X1)
height = abs(y2 - y1)
P = 2 * (side + height)
S = side * height
print(P)
print(S)