n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

sum_even = 0
prod_even = 1

for i in range(0, n, 2):
    sum_even = sum_even + a[i]
    prod_even = prod_even * a[i]

print(sum_even)
print(prod_even)