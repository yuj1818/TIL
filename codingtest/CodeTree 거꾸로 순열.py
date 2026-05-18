n = int(input())
visited = [0] * (n + 1)
ans = []

def choose(x):
    if x == n + 1:
        print(' '.join(map(str, ans)))
        return
    for i in range(n, 0, -1):
        if visited[i]: continue
        visited[i] = 1
        ans.append(i)
        choose(x + 1)
        ans.pop()
        visited[i] = 0

choose(1)
