# Proc11
def minmax(x, y):
    if x < y:
        return x, y
    return y, x

a = float(input())
b = float(input())
c = float(input())
d = float(input())

lo1, hi1 = minmax(a, b)
lo2, hi2 = minmax(c, d)

min_all, _ = minmax(lo1, lo2)
_, max_all = minmax(hi1, hi2)

print(min_all)
print(max_all)