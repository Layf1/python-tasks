# Err7. Читать ввод, пока не введено целое число. Ошибки не роняют программу. Вывести число.
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")
print(number)