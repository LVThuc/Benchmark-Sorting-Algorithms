arr = []
n = 0
def merge(l, m, r):
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

def mergeSort(l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(l, m)
        mergeSort(m+1, r)
        merge(l, m, r)


filename = "input.inp"
with open('input.inp') as f:
    n = int(f.readline())
    line = f.readline()
    data = line.split()
    for i in range(n):
        arr.append(int(data[i]))
mergeSort(0, n - 1)