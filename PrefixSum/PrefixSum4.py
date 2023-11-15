# 11659

M, N = map(int, input().split())
# Original 
A = list(map(int, input().split()))
# Prefix Sum
D = [0]
temp = 0

for i in A:
    temp += i
    D.append(temp)

for _ in range(N):
    s, e = map(int, input().split())
    print(D[e] - D[s-1])