#Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей.
#Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.
X = float(input())
Y = float(input())
A = float(input())
price_per_kgX = A / X
price_per_kgY = A / Y
how_much = price_per_kgX / price_per_kgY
print(price_per_kgX)
print(price_per_kgY)
print(how_much)