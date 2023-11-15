# 11660
import sys
input = sys.stdin.readline
# n -> N * N array , m -> Number of Answer
n, m = map(int, input().split())
A = [[0] * (n + 1)] # original list
D = [[0] * (n + 1) for _ in range(n + 1)] # Prefix sum list

# Input Original list 
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# Fill prefix sum list
for i in range(1, n+1):
    for j in range(n + 1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

# Get answer 
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)