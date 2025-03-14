from num_gen import *
import time
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while array[j] > temp and j>=0:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = temp
    return array

def bubble_sort(arr):
    for i in range(len(arr)):
        sorted = True
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        if sorted:
            break

def selection_sort(array):
    size = len(array)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

def merge(arr, start, mid, end):
    start1 = start
    end1 = mid
    start2 = mid + 1
    end2 = end
    temp = []
    while(start1 <= end1 and start2 <= end2):
        if arr[start1] < arr[start2]:
            temp.append(arr[start1])
            start1 += 1
        else:
            temp.append(arr[start2])
            start2 += 1
    while start1 <= end1:
        temp.append(arr[start1])
        start1 += 1
    while start2 <= end2:
        temp.append(arr[start2])
        start2 += 1
    for i in range(len(temp)):
        arr[start + i] = temp[i] 
    

def merge_sort_recursive(arr, start, end):
    if start < end:
        merge_sort_recursive(arr, start, (start+end)//2)
        merge_sort_recursive(arr, (start+end)//2+1, end)
        merge(arr, start, (start+end)//2, end)


def merge_sort(arr):
    merge_sort_recursive(arr, 0, len(arr)-1)

# arr = generate(1000000)
# begin = time.time()
# merge_sort(arr)
# end = time.time()
# print(arr)
# print(1000*(end-begin))