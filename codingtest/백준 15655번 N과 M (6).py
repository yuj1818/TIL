import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
s = []

def dfs(l, i):
    if l == m:
        print(' '.join(map(str, s)))
        return
    for j in range(i, n):
        if arr[j] in s: continue
        s.append(arr[j])
        dfs(l + 1, j + 1)
        s.pop()

dfs(0, 0)