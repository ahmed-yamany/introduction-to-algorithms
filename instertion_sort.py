import time

def insertion_sort_non_decreasing(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

    return array

start = time.time()
s = insertion_sort_non_decreasing([1, 5, 9, 4, 3, 6, 1])
end = time.time()

print(s)
print(end - start)


def insertion_sort_non_increasing(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while array[j] < key and j >= 0:
            array[j + 1] = array[j]
            j = j -1
        array[j + 1] = key
    return array


insertion_sort_non_increasing([31, 41, 59, 41, 58])
