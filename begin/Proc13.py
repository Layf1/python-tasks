# Proc13
def sort_dec3(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return a, b, c

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

a1, b1, c1 = sort_dec3(a1, b1, c1)
print(a1)
print(b1)
print(c1)

a2, b2, c2 = sort_dec3(a2, b2, c2)
print(a2)
print(b2)
print(c2)