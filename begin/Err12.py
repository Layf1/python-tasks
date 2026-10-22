# Err12. При ошибке вывести текст исключения и тип через as e и type(e). При успехе - число.
try:
    number = int(input())
    print(number)
except ValueError as e:
    print(e)
    print(type(e))