import random

number = int(input('input number N - '))
subsequence = []
positions = []
_sum = 0
for i in range(number):
    subsequence.append(random.randint(-number, number))

# with open('file.txt', 'w+') as f:
#     _set = set()
#     for i in range(25):
#         _set.add(random.randint(0, 25))
#     for i in _set:
#         f.write(f'{i}\n')

with open('file.txt', 'r') as f:
    for i in f:
        if int(i) < len(subsequence):
            positions.append(int(i))
            _sum += subsequence[int(i)]
print(f'subsequence - {subsequence}')
print(f'positions - {positions}')
print(f'sum - {_sum}')
