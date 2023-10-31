# 10986
# n -> Number of list, m -> divide num
n, m = map(int, input().split())
A = list(map(int, input().split()))  # original list
S = [0] * n  # Prefix sum list
C = [0] * m # Number of Remainder 

# Before fill Prefix sum, should put the first value within original list 
S[0] = A[0]
answer = 0

# Fill Prefix sum list 
for i in range(1, n):
    S[i] = S[i - 1] + A[i]

# Caclulate remainder and add to C list 
for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

# can calculate the number of remainder is 0 when sum particular range 
# number of 0 remainder is combination of same number  
for i in range(m):
    if C[i] > 1:
        answer += C[i] * (C[i] - 1) // 2

print(answer)
