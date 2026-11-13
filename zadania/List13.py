n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

removed = a.pop()
print(removed)
print(a)