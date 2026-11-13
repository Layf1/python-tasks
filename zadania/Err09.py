# Err9. Возраст от 0 до 120 через raise и catch ValueError.
try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
    print(f"Принято: {age}")
except ValueError as e:
    print(f"Отклонено: {e}")