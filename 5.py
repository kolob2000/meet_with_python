import math

num = int(input('input integer digit - '))


def fibonacci(n):
    fi = (1 + math.sqrt(5)) / 2
    psi = -(1 / fi)
    return round((fi ** n - psi ** n) / math.sqrt(5))


for i in range(-num, num + 1):
    print(i, end='\t\t')

print()
for i in range(-num, num + 1):
    print(fibonacci(i), end='\t\t')
