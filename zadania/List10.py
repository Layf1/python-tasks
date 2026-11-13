n = int(input())
a = []
for i in range(n):
    a.append(input())

longest = a[0]
shortest = a[0]

for s in a:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s

print(longest, len(longest))
print(shortest, len(shortest))