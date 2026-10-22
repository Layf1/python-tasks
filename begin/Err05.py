# Err5. Прочитать строку и индекс. Вывести символ. Если индекса нет, вывести "Нет такого символа".
try:
    text = input()
    index = int(input())
    print(text[index])
except IndexError:
    print("Нет такого символа")