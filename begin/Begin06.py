#Даны длины ребер a, b, c прямоугольного параллелепипеда. 
#Найти его объем V= a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).
height = float(input("Высота"))
length = float(input("Длинна"))
width = float(input("Ширина"))
volume = height * length * width
surface = 2 * (height * length + length * width + width * height)