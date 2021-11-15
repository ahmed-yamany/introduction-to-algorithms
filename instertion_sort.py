def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j = j - 1
        array[j + 1] = key

    return array


insertion_sort([5, 2, 4, 6, 1, 3])
