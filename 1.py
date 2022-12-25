def bbp_formula(d):
    return sum(
        [(1 / 16 ** i) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6)) for i in
         range(int(1 / d))])


if __name__ == '__main__':
    print(bbp_formula(0.001))
