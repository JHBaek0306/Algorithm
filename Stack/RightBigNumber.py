# 17298
import sys
input = sys.stdin.readline

n = int(input()) # number of list
ans = [0] * n # answer list 
A = list(map(int, input().split())) # original list 
myStack = [] # using stack to find out target number 

# put the index not the value of the list 
for i in range(n):
    while myStack and A[myStack[-1]] < A[i]: # number exist in Stack and last index number is smaller than original list number 
        ans[myStack.pop()] = A[i] 
    myStack.append(i)

while myStack: # fill -1 remainder index 
    ans[myStack.pop()] = -1

result = ''

for i in range(n):
    result += str(ans[i])+' '

print(result)