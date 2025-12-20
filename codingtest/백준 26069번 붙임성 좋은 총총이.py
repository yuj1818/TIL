import sys
input = sys.stdin.readline
n = int(input())
dancing = set(['ChongChong'])
for _ in range(n):
    a, b = input().rstrip().split()
    if a in dancing: dancing.add(b)
    elif b in dancing: dancing.add(a)
print(len(dancing))