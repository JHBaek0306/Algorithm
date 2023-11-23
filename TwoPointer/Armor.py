# 1940
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = 0
s, e = 0, N - 1
while s < e:
    if A[s] + A[e] == M:
        cnt += 1
        s += 1
        e -= 1
    elif A[s] + A[e] < M:
        s += 1
    elif A[s] + A[e] > M:
        e -= 1

print(cnt)