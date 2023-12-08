# 1934
import sys
input = sys.stdin.readline
import math

T = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for i in range(T):
    A, B = map(int, input().split())
    result = A * B / gcd(A, B)
    print(int(result))