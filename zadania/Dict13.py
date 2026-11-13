# Dict13. Построить словарь из N троек: название, цена, количество (значение — список из двух чисел).
# Вывести суммарную стоимость склада и название самого дорогого по стоимости предмета.

n = int(input())
warehouse = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    warehouse[name] = [price, qty]

total_cost = 0
max_item_cost = -1
best_item = ""

for name, (price, qty) in warehouse.items():
    item_cost = price * qty
    total_cost += item_cost
    if item_cost > max_item_cost:
        max_item_cost = item_cost
        best_item = name

print(total_cost)
print(best_item)