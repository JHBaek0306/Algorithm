#2003

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
    if D[right] - D[left - 1 if left - 1 > 0 else 0] == M :
        cnt += 1
        right += 1
    elif D[right] - D[left - 1 if left - 1 > 0 else 0] > M:
        left += 1
    elif D[right] - D[left - 1 if left - 1 > 0 else 0] < M:
        right += 1

print(cnt)