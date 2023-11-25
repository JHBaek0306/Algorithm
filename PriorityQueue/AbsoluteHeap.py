# 11286
import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    x = int(input())
    if x == 0:
        if myQueue.empty():
            print('0')
        else:
            tmp = myQueue.get()
            print(str((tmp[1])))
    
    else:
        myQueue.put((abs(x), x))