import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def dfs(s, d):
    if d == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(s, n + 1):
        arr.append(i)
        dfs(i, d + 1)
        arr.pop()

dfs(1, 0)