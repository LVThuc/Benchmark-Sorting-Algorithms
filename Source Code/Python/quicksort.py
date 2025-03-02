array = []
n = 0
def partition(low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(low, high):
    if low < high:
        pi = partition(low, high)
        quicksort(low, pi - 1)
        quicksort(pi + 1, high)
filename = "input.inp"
with open('input.inp') as f:
    n = int(f.readline())
    line = f.readline()
    data = line.split()
    for i in range(n):
        array.append(int(data[i]))
quicksort(0, n - 1)