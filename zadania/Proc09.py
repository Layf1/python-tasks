# Proc9
def digit_count(k):
    if k == 0:
        return 1
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count

def add_left_digit(d, k):
    return d * (10 ** digit_count(k)) + k

k = int(input())
d1 = int(input())
d2 = int(input())

k = add_left_digit(d1, k)
print(k)

k = add_left_digit(d2, k)
print(k)