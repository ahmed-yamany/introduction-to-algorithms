import time


def selection_sort(array):
    ar_sort = []
    for i in range(len(array)):
        ar_min = min(array)
        ar_sort.append(ar_min)
        array.remove(ar_min)
    return ar_sort


start = time.time()
s = selection_sort([1, 5, 9, 4, 3, 6, 1])
end = time.time()

print(s)
print(end - start)
