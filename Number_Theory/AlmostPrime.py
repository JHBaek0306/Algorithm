# 1456
import sys
input = sys.stdin.readline
import math

a, b = map(int, input().split())
A = [0] * 10000001

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):
        A[j] = 0

cnt = 0

for i in range(2, 10000001):
    if A[i] != 0:
        tmp = A[i]
        while A[i] <= b / tmp: 
            if A[i] >= a / tmp:
                cnt += 1
            tmp = tmp * A[i]

print(cnt)
