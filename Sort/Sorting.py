# 2751
import sys
input = sys.stdin.readline

def merge(arr, low, high):
    temp = []
    mid = (low + high) // 2
    i, j = low, mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for k in range(low, high + 1):
        arr[k] = temp[k - low]

    return arr


def mergeSort(arr, low, high):
    if (low >= high):
        return  # base case

    mid = (low + high) // 2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)

    sorted_array = merge(arr, low, high)

    return sorted_array

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

sortedArr = mergeSort(arr, 0, len(arr) -1 )

for num in sortedArr:
    print(num, end="\n")