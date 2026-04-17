def solution(n, infection, edges, k):
    graph = [[] for _ in range(n + 1)]
    for a, b, t in edges:
        graph[a].append((b, t))
        graph[b].append((a, t))

    def virus(infected, type):
        ni = set(infected)
        q = list(infected)
        while q:
            x = q.pop(0)
            for nx, t in graph[x]:
                if t == type and nx not in ni:
                    ni.add(nx)
                    q.append(nx)
        return ni

    def dfs(infected, limit):
        cnt = len(infected)
        if limit == 0: return cnt
        mv = cnt
        for t in [1, 2, 3]:
            ni = virus(infected, t)
            mv = max(mv, dfs(ni, limit - 1))
        return mv

    return dfs(set([infection]), k)

print(solution(10, 1, [[1, 2, 1], [1, 3, 1], [1, 4, 3], [1, 5, 2], [5, 6, 1], [5, 7, 1], [2, 8, 3], [2, 9, 2], [9, 10, 1]], 2))
# 6
