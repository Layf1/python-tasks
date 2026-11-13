# Err6. Строка и индекс: нечисловой индекс - "Ошибка ввода", индекс вне границ - "Нет такого символа".
try:
    text = input()
    index = int(input())
    print(text[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")