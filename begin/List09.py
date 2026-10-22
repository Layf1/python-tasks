n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

avg = sum(a) / n
k = 0

for x in a:
    if x > avg:
        print(x)
        k = k + 1

print(k)