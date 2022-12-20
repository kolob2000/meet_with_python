def decimal_to_digit(digit: int) -> str:
    binary = ''
    while digit != 0:
        digit, reminder = divmod(digit, 2)
        binary = str(reminder) + binary
    return binary


print(decimal_to_digit(46))
