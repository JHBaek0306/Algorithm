# 1920
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()    
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    s = 0
    e = N - 1
    while s <= e:
        mid_idx = (s + e) // 2
        mid_val = A[mid_idx]
        if mid_val > target:
            e = mid_idx - 1
        elif mid_val < target:
            s = mid_idx + 1
        else :
            find = True
            break
    if find:
        print(1)
    else : 
        print(0)