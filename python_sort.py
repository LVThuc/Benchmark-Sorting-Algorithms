import numpy as np
import time
import json
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]


    i = 0   
    j = 0  
    k = l  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def median_of_three(arr, low, mid, high):
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            return mid
        elif arr[low] < arr[high]:
            return high
        else:
            return low
    else:
        if arr[low] < arr[high]:
            return low
        elif arr[mid] < arr[high]:
            return high
        else:
            return mid

def partition(arr, low, high):
    mid = (low + high) // 2
    pivot_index = median_of_three(arr, low, mid, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr,l,h):

    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition( arr, l, h )
 
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 

        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
            
filename = "input.inp"
arr = []
with open('input.inp') as f:
    tt = f.readlines()
    for line in tt:
        data = line.split()
        data = [int(i) for i in data]
        arr.append(data)
Heapsort = []
Mergesort = []
Quicksort = []
Built_in_Python_Sort = []
Numpy_Sort = []
for array in arr:
    n = len(array)
    arr1 = array.copy()
    arr2 = array.copy()
    arr3 = array.copy()
    arr4 = array.copy()
    arr5 = np.array(arr.copy())

    start_time = time.time_ns()
    heapSort(arr1)
    end_time = time.time_ns()
    Heapsort.append((end_time - start_time) / 1000000)
    print("HeapSort --- %s milliseconds ---" % ((end_time - start_time) / 1000000))

    start_time = time.time_ns()
    mergeSort(arr2, 0, n - 1)
    end_time = time.time_ns()
    Mergesort.append((end_time - start_time) / 1000000)
    print("MergeSort --- %s milliseconds ---" % ((end_time - start_time) / 1000000))

    start_time = time.time_ns()
    quickSort(arr3, 0, n - 1)
    end_time = time.time_ns()
    Quicksort.append((end_time - start_time) / 1000000)
    print("QuickSort --- %s milliseconds ---" % ((end_time - start_time) / 1000000))

    start_time = time.time_ns()
    arr4.sort()
    end_time = time.time_ns()
    Built_in_Python_Sort.append((end_time - start_time) / 1000000)
    print("Built-in Sort --- %s milliseconds ---" % ((end_time - start_time) / 1000000))

    start_time = time.time_ns()
    np.sort(arr5)
    end_time = time.time_ns()
    Numpy_Sort.append((end_time - start_time) / 1000000)
    print("NumPy Sort --- %s milliseconds ---" % ((end_time - start_time) / 1000000))
    print(" ")
# Output:
with open("Heapsort.json", "w", encoding="utf-8") as f:
    json.dump(Heapsort, f, ensure_ascii=False, indent=4)

with open("Mergesort.json", "w", encoding="utf-8") as f:
    json.dump(Mergesort, f, ensure_ascii=False, indent=4)

with open("Quicksort.json", "w", encoding="utf-8") as f:
    json.dump(Quicksort, f, ensure_ascii=False, indent=4)

with open("Built_in_Python_Sort.json", "w", encoding="utf-8") as f:
    json.dump(Built_in_Python_Sort, f, ensure_ascii=False, indent=4)

with open("Numpy_Sort.json", "w", encoding="utf-8") as f:
    json.dump(Numpy_Sort, f, ensure_ascii=False, indent=4)