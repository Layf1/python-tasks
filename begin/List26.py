n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

avg = sum(a) / len(a) if a else 0
greater_than_avg = [x for x in a if x > avg]

print(greater_than_avg)
print(avg)