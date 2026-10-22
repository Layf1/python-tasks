# Err11. Два числа, частное, кортеж ошибок "Посчитать не удалось", в else вывод с 2 знаками.
try:
    a = int(input())
    b = int(input())
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")