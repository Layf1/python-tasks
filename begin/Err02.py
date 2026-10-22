#Прочитать два целых числа и вывести частное (1 знак после точки). Деление на ноль - сообщение.
try:
    a = int(input())
    b = int(input())
    print(f"{a / b:.1f}")
except ZeroDivisionError:
    print("Делить на ноль нельзя")