import time
start_time = time.time()
arr = []
def heapify(n, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2
 
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
        heapify(n, largest)
 
n = 0
def heapSort():

 
    for i in range(n // 2, -1, -1):
        heapify(n, i)
 
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(i, 0)

filename = "input.inp"
with open('input.inp') as f:
    n = int(f.readline())
    line = f.readline()
    data = line.split()
    for i in range(n):
        arr.append(int(data[i]))
heapSort()