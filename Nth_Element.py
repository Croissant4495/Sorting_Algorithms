from sorting import partition

def quick_select_rec(arr, i, j, k):
    pivot = partition(arr, i, j)
    if pivot == k:
        return arr[pivot]
    elif k< pivot:
        return quick_select_rec(arr, i, pivot, k)
    else:
        return quick_select_rec(arr, pivot+1, j, k)

def quick_select(arr, k):
    return quick_select_rec(arr, 0, len(arr), k -1)