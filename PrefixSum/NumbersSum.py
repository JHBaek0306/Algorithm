#2003
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
D = [0]
temp = 0

for i in A:
    temp += i
    D.append(temp)
 
left, right = 0, 1
cnt = 0

while(left < right and right <= N):
    if D[right] - D[left] == M :
        cnt += 1
        right += 1
    elif D[right] - D[left] > M:
        left += 1
    elif D[right] - D[left] < M:
        right += 1

print(cnt)