while 1:
    predicates = list(map(bool, map(int, input('input three logical(digit) predicates separated by coma - ').split())))
    if len(predicates) != 3:
        print('invalid input')
    else:
        a, b, c = predicates
        print('predicates - ', *predicates)
        print(not (a or b or c) == (not a and not b and not c))
