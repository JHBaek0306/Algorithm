# 1253
import sys
input = sys.stdin.readline

N = int(input())
result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    s = 0
    e = N - 1
    while s < e:
        if A[s] + A[e] == A[k]:
            if s != k and e != k:
                result += 1
                break
            elif s == k:
                s += 1
            elif e == k:
                e -= 1
        elif A[s] + A[e] < A[k]:
            s += 1
        else:
            e -= 1

print(result)