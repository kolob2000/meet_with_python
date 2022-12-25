def sieve_of_eratosthenes(number: int) -> list:
    row = {i: '_' for i in range(2, number + 1) if i == 2 or i > 2 and i % 2 != 0}
    # use a dict cause a list too expensive operation for deletion items
    i = 2
    while True:
        if i ** 2 > number:
            break
        elif i != 2 and i % 2 == 0:
            i += 1
            continue

        for j in range(i, number + 1, 2):
            if j * i > number:
                break
            elif (j * i) in row:
                del row[j * i]
        i += 1
    return list(row)


def prime_factorization(number: int) -> list:
    prime_numbers = sieve_of_eratosthenes(number)
    if number in prime_numbers: return [number]
    prime_factors = [i for i in prime_numbers if number % i == 0]
    return prime_factors


if __name__ == '__main__':
    print(prime_factorization(2200))
    print(prime_factorization(239))
    print(prime_factorization(100))
