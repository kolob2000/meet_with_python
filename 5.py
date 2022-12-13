import math

x1, y1 = list(map(int, input('input coords(x1 y1) for first point separated by coma - ').split()))
x2, y2 = list(map(int, input('input coords(x2 y2) for first points separated by coma - ').split()))

print(round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3))
