import functools

array = [2, 3, 5, 9, 3]
accumulator = 0
for i in array[1::2]:
    accumulator += i
print(f'sum from cycle - {accumulator}')

print(f'sum from reducer - {functools.reduce(lambda x, y: x + y, array[1::2])}')
