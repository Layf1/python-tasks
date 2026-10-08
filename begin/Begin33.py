#Известно, что X кг конфет стоит A рублей. 
#Определить, сколько стоит 1 кг и Y кг этих же конфет.
X = float(input())
A = float(input())
Y = float(input())
price_per_kg = A / X
price_per_Y = price_per_kg * Y
print(price_per_kg)
print(price_per_Y)
