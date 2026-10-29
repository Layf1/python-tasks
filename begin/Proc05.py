# Proc5
def rect_ps(x1, y1, x2, y2):
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    p = 2 * (w + h)
    s = w * h
    return p, s

for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    p, s = rect_ps(x1, y1, x2, y2)
    print(p)
    print(s)