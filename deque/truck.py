# 13335
from collections import deque

N, W, L = map(int, input().split())
cars = list(map(int, input().split()))
bridge = deque(0 for _ in range(W))

time = 0
idx = 0
while idx < N:
    time += 1
    bridge.popleft()

    if sum(bridge) + cars[idx] <= L:
        bridge.append(cars[idx])
        idx += 1
    else :
        bridge.append(0)

while bridge:
    time += 1
    bridge.popleft()

print(time)
