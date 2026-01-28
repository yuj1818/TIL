import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [1] + list(map(int, input().split()))
res = 0

def dfs(s, t, i):
    global res
    if t > m: return
    if t <= m: res = max(res, s)
    if i <= n - 1: dfs(s + arr[i + 1], t + 1, i + 1)
    if i <= n - 2: dfs((s // 2) + arr[i + 2], t + 1, i + 2)

dfs(1, 0, 0)
print(res)