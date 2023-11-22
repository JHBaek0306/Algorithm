# 5430
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())

    arr = deque(input().strip()[1:-1].split(","))
    if n == 0:
        arr = deque()
    
    # if reverse is odd reverse the arraay
    reverse = 0
    flag = True

    for k in p:
        if not arr:
            print("error")
            flag = False
            break

        if k == "R":
            reverse += 1
        elif k == "D" and reverse % 2 == 0:
            arr.popleft()
        elif k == "D" and reverse % 2 == 1:
            arr.pop()
        else :
            print("error")
            flag = False
            break
    
    if reverse % 2 == 1:
        arr.reverse()
    if flag:
        print('[' + ",".join(arr) + ']')
