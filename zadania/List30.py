n = int(input())
s = []
for i in range(n):
    s.append(input())

lengths = [len(string) for string in s]
print(lengths)