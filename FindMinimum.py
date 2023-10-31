# 11003
# Finding minumum with moving window 
# Using deque 
from collections import deque

# Size of index, size of window 
N, L = map(int, input().split())
myDeque = deque()
myIdx = list(map(int, input().split()))

for i in range(N):
    # Compare value, if myIdx value has no chance to be minumum pop it 
    while myDeque and myDeque[-1][0] > myIdx[i]:
        myDeque.pop()
    myDeque.append(myIdx[i], i)
    # Compare index, if index exceed the size of window pop it
    if myDeque[0][1] <= i - L:
        myDeque.popleft
    print(myDeque[0][0], end=" ")
