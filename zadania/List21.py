n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

positives = [x for x in a if x > 0]
print(positives)
print(len(positives))