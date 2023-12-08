# 1850
import sys
input = sys.stdin.readline
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())
result = gcd(a, b)

for _ in range(result):
    print(1, end="")