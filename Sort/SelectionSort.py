# 1427
import sys
input = sys.stdin.readline

A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i + 1, len(A)):
        if A[Max] < A[j]:
            Max = j
    
    if A[i] < A[Max]:
        A[i], A[Max] = A[Max], A[i]

for i in range(len(A)):
    print(A[i], end="")