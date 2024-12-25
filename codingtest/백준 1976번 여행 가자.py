import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    plan = list(map(lambda x: int(x) - 1, input().split()))

    def dfs(s):
        visited[s] = 1
        for i in range(n):
            if graph[s][i] and not visited[i]:
                dfs(i)

    visited = [0] * n
    dfs(plan[0])
    for p in plan:
        if not visited[p]: return 'NO'
    return 'YES'

print(main())