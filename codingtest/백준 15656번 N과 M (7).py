import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(map(int, input().split()))
s = []
cnt = len(a)

def dfs(x):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(x, cnt):
        s.append(a[i])
        dfs(0)
        s.pop()

dfs(0)
