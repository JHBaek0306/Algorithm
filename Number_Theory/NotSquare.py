#1016
import sys
input = sys.stdin.readline
import math

Min, Max = map(int, input().split())
A = [False] * (Max - Min + 1) 

for i in range(2, int(math.sqrt(Max) + 1)):
    pow = i * i
    start_index = int(Min / pow)
    if Min % pow != 0:
        start_index += 1
    for j in range(start_index, int(Max / pow) + 1):
        A[int((j * pow) - Min)] = True

cnt = 0

for i in range(0, Max - Min + 1):
    if not A[i]:
        cnt += 1

print(cnt)