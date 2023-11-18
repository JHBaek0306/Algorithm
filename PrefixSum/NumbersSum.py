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
length = sys.maxsize

while(left <= right and right <= N):
    if D[right] - D[left] >= M:
        length = min(length, right - left)
        left += 1
    else:
        right += 1

if(length == sys.maxsize):
    length = 0
print(length)