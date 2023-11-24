# 12891
import sys
input = sys.stdin.readline

check = [0] * 4
myList = [0] * 4
checkSecret = 0

def add(c):
    global check, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == check[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == check[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == check[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == check[3]:
            checkSecret += 1

def remove(c):
    global check, myList, checkSecret
    if c == 'A': 
        if myList[0] == check[0]:
            checkSecret -= 1
        myList[0] -= 1 
    elif c == 'C':
        if myList[1] == check[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == check[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == check[3]:
            checkSecret -= 1    
        myList[3] -= 1    

S, P = map(int, input().split())
A = list(input())
check = list(map(int, input().split()))
result = 0

for i in range(4):
    if check[i] == 0:
        checkSecret += 1
        
for i in range(P):
    add(A[i])

if checkSecret == 4:
    result += 1

for i in range(P, S):
    j = i - P
    add(A[i])
    remove(A[j])
    if checkSecret == 4:
        result += 1

print(result)

