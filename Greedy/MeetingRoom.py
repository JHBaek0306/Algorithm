# 1931
import sys
input = sys.stdin.readline

N = int(input())
A = [[0] * 2 for _ in range(N)]
    
for i in range(N):
    s, e = map(int, input().split())
    A[i][0] = e
    A[i][1] = s

A.sort()
end = -1
cnt = 0
for i in range(N):
    if A[i][1] >= end:
        end = A[i][0] 
        cnt += 1

print(cnt)