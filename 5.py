def str_to_array(file_name: str) -> list:
    with open(file_name, 'r') as f:
        file_name = f.read()
        equal = file_name.index('=')
        return [i.strip() for i in file_name[:equal].split('+')]


def string_to_tuple(poly_str: str) -> tuple:
    if 'x' in poly_str:
        idx = poly_str.index('x')
        digit = poly_str[0:idx]
        arg = poly_str[idx:]
        return digit, arg
    elif poly_str.isdigit():
        return poly_str, 'is_digit'


def polynomial_reducer(first_poly, second_poly):
    new_polynomial = []
    for i in first_poly:
        summ = 0
        for j in second_poly:
            if i[1] == j[1]:
                summ += int(j[0]) if j[0] != '' else 1
        summ += int(i[0]) if i[0] != '' else 1
        monomial = f'{summ if summ > 1 else ""}{i[1] if i[1] != "is_digit" else ""}'
        new_polynomial.append(monomial)
    return f'{" + ".join(new_polynomial)} = 0'


def polynomial_parser(first_file: str, second_file: str):
    first_array = list(map(string_to_tuple, str_to_array(first_file)))
    second_array = list(map(string_to_tuple, str_to_array(second_file)))
    if len(first_array) < len(second_array):
        first_array, second_array = second_array, first_array

    return polynomial_reducer(first_array, second_array)


if __name__ == '__main__':
    print('----- old -----')
    with open('poly1.txt', 'r') as f:
        print(f.readline())
    with open('poly2.txt', 'r') as f:
        print(f.readline())
    print('----- new -----')
    print(polynomial_parser('poly1.txt', 'poly2.txt'))
