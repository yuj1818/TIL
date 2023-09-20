T = int(input())

def dfs(s):
    stack.append(s)
    visited[s] = 1
    for w in adj_l[s]:
        if not visited[w]:
            dfs(w)

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj_l = [[] for _ in range(N + 1)]
    pairs = list(map(int, input().split()))
    for i in range(M):
        adj_l[pairs[i * 2]].append(pairs[i * 2 + 1])
        adj_l[pairs[i * 2 + 1]].append(pairs[i * 2])
    people = [i for i in range(1, N + 1)]
    ans = 0
    while people:
        stack = []
        visited = [0] * (N + 1)
        dfs(people[0])
        people = list(set(people) - set(stack))
        ans += 1
    print(f'#{tc} {ans}')