# 2164
from collections import deque

N = int(input())
myDeque = deque(range(1, N+ 1))

while len(myDeque) != 1:
    myDeque.popleft()
    myDeque.append(myDeque.popleft())
    
print(myDeque.pop())
