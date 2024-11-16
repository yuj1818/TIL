import sys
input = sys.stdin.readline
A, B = 0, 0
last = 'D'

for a, b in zip(map(int, input().split()), map(int, input().split())):
    if a > b: 
        A += 3
        last = 'A'
    elif a < b: 
        B += 3
        last = 'B'
    else: 
        A += 1
        B += 1
        
print(A, B)
print(last if A == B else 'A' if A > B else 'B')