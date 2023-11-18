# 1806 
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))
D = [0]

temp = 0
for i in A:
    temp += i
    D.append(temp)

left, right = 0, 1
count = 0
while(left <= right and right <= N):
    if D[right] - D[left] == S:
        count += 1
        right += 1
    elif D[right] - D[left] > S:
        left += 1
    elif D[right] - D[left] < S:
        right += 1

print(count)