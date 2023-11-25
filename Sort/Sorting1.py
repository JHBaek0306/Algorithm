# 2750
import sys
input = sys.stdin.readline

N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-i-1):
        if A[j] > A[j+1]:
            tmp = A[j]
            A[j] = A[j+1]
            A[j+1] = tmp

for n in A:
    print(n)

         
