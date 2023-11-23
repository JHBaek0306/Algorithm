# 2018
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
s, e = 1, 1
sum = 1

while s <= e and e <= n:
    if sum == n:
        cnt += 1
        e += 1
        sum += e
    elif sum < n:
        e += 1
        sum += e
    elif sum > n:
        sum -= s
        s += 1
        
print(cnt)