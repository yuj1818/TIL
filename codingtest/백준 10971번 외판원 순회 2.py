import sys

input = sys.stdin.readline


def dfs(x, cnt, dist):
    global ans
    if cnt == n:
        if W[x][0] != 0:
            ans = min(ans, dist + W[x][0])
        return
    for i in range(n):
        nxt = W[x][i]
        if not visited[i] and nxt != 0:
            visited[i] = 1
            dfs(i, cnt + 1, dist + nxt)
            visited[i] = 0


n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
visited[0] = 1
ans = 10**6 * 10 + 1
dfs(0, 1, 0)
print(ans)
