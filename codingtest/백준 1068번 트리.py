import sys
input = sys.stdin.readline

def dfs(x):
    par[x] = -2
    for i in range(n):
        if x == par[i]: dfs(i)

n = int(input())
par = list(map(int, input().split()))
d = int(input())
dfs(d)
cnt = 0
for i in range(n):
    if par[i] != -2 and i not in par: cnt += 1
print(cnt)