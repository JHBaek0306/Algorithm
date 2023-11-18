# 2599
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
D = [0]

temp = 0
for i in A:
    temp += i
    D.append(temp)

max = -sys.maxsize

for i in range(len(D) - K):
    if D[i+K] - D[i] > max:
        max = D[i+K] - D[i]

print(max)