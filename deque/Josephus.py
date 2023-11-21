# 1158
from collections import deque

N, K = map(int, input().split())
myDeque = deque(range(1, N + 1))
output = []

while myDeque:
    for _ in range(K -1):
        myDeque.append(myDeque.popleft())
    output.append(myDeque.popleft())

print(str(output).replace("[", "<").replace("]", ">"))