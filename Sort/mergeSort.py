# 2751
import sys

input = sys.stdin.readline


def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)

        sortedArray = merge(arr, low, high)

        return sortedArray


def merge(arr, low, high):
    mid = (low + high) // 2
    i, j = low, mid + 1
    output = []

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            output.append(arr[i])
            i += 1
        else:
            output.append(arr[j])
            j += 1

    while i <= mid:
        output.append(arr[i])
        i += 1

    while j <= high:
        output.append(arr[j])
        j += 1

    for k in range(low, high + 1):
        arr[k] = output[k - low]

    return arr


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

sortedArr = mergeSort(arr, 0, len(arr) - 1)

for num in sortedArr:
    print(num, end="\n")
