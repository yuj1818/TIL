from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    edge = []
    for s, e in combinations([i for i in range(N)], 2):
        edge.append([s, e, ((X[s] - X[e]) ** 2 + (Y[s] - Y[e]) ** 2) * E])
    edge.sort(key=lambda x: x[2])
    parents = [i for i in range(N)]

    def find_set(x):
        if parents[x] == x:
            return x
        parents[x] = find_set(parents[x])
        return parents[x]

    def union(x, y):
        x = find_set(x)
        y = find_set(y)

        if x == y:
            return
        if x < y:
            parents[y] = x
        else:
            parents[x] = y

    cnt = 0
    t_cost = 0
    for s, e, w in edge:
        if find_set(s) != find_set(e):
            cnt += 1
            t_cost += w
            union(s, e)
            if cnt == N - 1:
                break
    print(f'#{tc} {t_cost:.0f}')