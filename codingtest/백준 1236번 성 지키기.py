import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a,b=0,0
arr=[input().rstrip() for _ in range(n)]
for i in range(n):
    if 'X' in arr[i]: continue
    a+=1
for x in zip(*arr):
  if 'X' in x: continue
  b+=1
print(max(a,b))
