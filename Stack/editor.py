#1406
import sys
input = sys.stdin.readline

stack1 = list(input())
stack2 = []

n = int(input())

for _ in range(n):
    command = list(input().split())
    if command[0] == "L" :
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == "D" :
        if stack2:
            stack1.append(stack2.pop()) 
    elif command[0] == "B" :
        if stack1:
            stack1.pop()
    elif command[0] == "P" :
        stack1.append(command[1])

stack1.extend(stack2)
print(''.join(stack1))