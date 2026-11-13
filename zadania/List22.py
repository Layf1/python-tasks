n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())

multiplied = [x * d for x in a]
equal_count = len([x for x in a if x == d])

print(multiplied)
print(equal_count)