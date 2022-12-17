number = int(input("input number N - "))
_sum = 0
subsequence = {}
for i in range(1, number + 1):
    subsequence.update({i: round((1 + 1 / i) ** i, 2)})
    _sum += (1 + 1 / i) ** i
print(subsequence)
print(f'Sum - {round(_sum, 2)}')
