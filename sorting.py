from num_gen import *

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
            if arr[j] > arr[j+1]:
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

def merge_insert_hybrid_recursive(arr, start, end, t):
    if start < end:
        if end - start < t:
            insertion_sort(arr[start:end+1])
        else:
            merge_insert_hybrid_recursive(arr, start, (start+end)//2, t)
            merge_insert_hybrid_recursive(arr, (start+end)//2+1, end, t)
            merge(arr, start, (start+end)//2, end)


def merge_sort(arr):
    merge_sort_recursive(arr, 0, len(arr)-1)

def merge_insert_hybrid_sort(arr, t):
    merge_insert_hybrid_recursive(arr, 0, len(arr)-1, t)

def swap(arr, i , j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, i, j):
    pivot = i
    while i < j:
        i +=1
        if i< len(arr) -1:
            while arr[i] < arr[pivot]:
                i +=1
        
        j -=1
        while arr[j] > arr[pivot]:
            j -=1

        if i<j:
            swap(arr, i, j)
    swap(arr, pivot, j)
    return j

def quick_sort_rec(arr, i, j):
    if i < j:
        pivot = partition(arr, i, j)
        quick_sort_rec(arr, i, pivot)
        quick_sort_rec(arr, pivot+1, j)

def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr))
