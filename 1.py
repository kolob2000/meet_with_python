while 1:
    day = int(input('input digit from 1 to 7 - '))
    if day in range(1, 8):
        break

    print('invalid digit')
if day in range(1, 6):
    print('working day')
else:
    print('weekend')
