number = input('input float numer - ')
_sum = 0
for i in number:
    if i.isdigit():
        _sum += int(i)

print(_sum)
