import random


def row_without_repeatitions(row: list) -> list:
    sieve = {}
    clean_row = []
    for i in row:
        if i in sieve:
            sieve[i] += 1
        else:
            sieve.setdefault(i, 0)
    for key, value in sieve.items():
        if not value:
            clean_row.append(key)

    return clean_row


if __name__ == '__main__':
    row = [random.randint(1, 8) for _ in range(10)]
    print(row)
    print(row_without_repeatitions(row))
