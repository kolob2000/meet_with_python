import random


def polynomial_gen(k: int) -> str:
    polynomial = []
    for i in range(k, 0, -1):
        var = random.randint(0, 20)
        if not var: continue
        var = var if var != 1 else ''
        if i != 1:
            polynomial.append(f'{var}x^{i}')
        else:
            polynomial.append(f'{var}x')
    var = random.randint(0, 20)
    if var:
        polynomial.append(str(var))

    return ' + '.join(polynomial) + ' = 0'


if __name__ == '__main__':
    polynomial = polynomial_gen(2)
    print(polynomial)
    with open('poly.txt', 'w') as f:
        f.write(polynomial)
