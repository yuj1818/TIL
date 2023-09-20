from collections import deque

T = int(input())

def go(s):
    q = deque()
    q.append(s)
    time = [float('inf') for _ in range(N + 1)]
    time[s] = 0
    while q:
        t = q.popleft()
        for i in range(1, N + 1):
            if G[i][t] and G[i][t] + time[t] < time[i]:
                time[i] = G[i][t] + time[t]
                q.append(i)
    return time

def back(s):
    q = deque()
    q.append(s)
    time = [float('inf') for _ in range(N + 1)]
    time[s] = 0
    while q:
        t = q.popleft()
        for i in range(1, N + 1):
            if G[t][i] and G[t][i] + time[t] < time[i]:
                time[i] = G[t][i] + time[t]
                q.append(i)
    return time

for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    G = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        G[x][y] = c
    ans = 0
    time1 = go(X)
    time2 = back(X)
    ans = max([x + y for x, y in zip(time1[1:], time2[1:])])
    print(f'#{tc} {ans}')