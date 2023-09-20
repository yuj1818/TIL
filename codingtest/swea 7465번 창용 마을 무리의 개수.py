T = int(input())

def dfs(s):
    stack.append(s)
    visited[s] = 1
    for i in range(N + 1):
        if adj[s][i] and not visited[i]:
            dfs(i)

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        adj[s][e] = 1
        adj[e][s] = 1
    people = [i for i in range(1, N + 1)]
    ans = 0
    while people:
        ans += 1
        stack = []
        visited = [0] * (N + 1)
        dfs(people[0])
        people = list(set(people) - set(stack))
    print(f'#{tc} {ans}')