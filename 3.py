import decimal as d

row_array = list(map(lambda x: round(x % int(x), 2), [1.1, 1.2, 3.1, 5, 10.01]))


def insertion_sort(array: list) -> list:
    for i in range(len(array) - 1):
        j = i + 1
        while j != 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


sorted_array = insertion_sort(row_array)

for i in range(len(sorted_array) - 1):
    if sorted_array[i] == 0:
        sorted_array.pop(i)

print(sorted_array[0] - sorted_array[-1])
