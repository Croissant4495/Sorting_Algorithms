def max_heapify(array, i, length):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < length and array[left] > array[largest]:
        largest = left
    if right < length and array[right] > array[largest]:
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)


def build_max_heap(array, length):
    for i in range(length // 2 - 1, -1, -1):
        max_heapify(array, i, length)


def heap_sort(array):
    length = len(array)

    build_max_heap(array, length)

    for i in range(length - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, 0, i)