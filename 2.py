def sum_of_pare(array: list[int]) -> list[int]:
    """
    get list of integer digits and return new list with
    multiplication of elements with elements that has negative some indexes
    :param array: list
    :return: new list
    """
    accumulator = []
    for i in range(int(len(array) // 2 + len(array) % 2)):
        accumulator.append(array[i] * array[-(i + 1)])
    return accumulator


help(sum_of_pare)
print(sum_of_pare([2, 3, 4, 5, 6]))
print(sum_of_pare([2, 3, 5, 6]))
