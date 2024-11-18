import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
visited = [0] * n
ans = 0

def dfs(w, cnt):
    global ans
    if w < 500:
        return
    if w - (n - cnt) * k >= 500:
        tmp = 1
        for i in range(1, n - cnt + 1): tmp *= i
        ans += tmp
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(w - k + a[i], cnt + 1)
            visited[i] = 0

dfs(500, 0)
print(ans)