#Дано целое число N (> 0). 
#Найти значение выражения 1.1 − 1.2 + 1.3 − ... (N слагаемых, знаки чередуются).

N = int(input())

total = 0.0

for i in range(1, N + 1):
    term = 1 + i / 10          
    if i % 2 == 0:             
        total -= term
    else:                      
        total += term

print(total)