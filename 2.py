while True:
    number = input('input numer N - ')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('invalid input, please repeat.')

mult = 1
for i in range(1, number + 1):
    mult *= i
    print(mult, end=' ')
