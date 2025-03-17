import sys
input = sys.stdin.readline

def dfs(s, visited, team):
    for w in matrix[s]:
        if visited[w] == team:
            visited[w] = 1
            dfs(w, visited, team)

def check(g1, g2):
    visited = [0] * n
    for a in g1: visited[a] = 'A'
    for b in g2: visited[b] = 'B'
    visited[g1[0]] = 1
    visited[g2[0]] = 1
    dfs(g1[0], visited, 'A')
    dfs(g2[0], visited, 'B')
    for x in visited:
        if x != 1: return False
    return True

def main():
    global n, matrix
    n = int(input())
    P = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        _, *nodes = list(map(lambda x: int(x) - 1, input().split()))
        matrix.append(nodes)
    min_dif = 100 * 10
    sig = 0
    for i in range(1 << n):
        g1 = []
        g2 = []
        for j in range(n):
            if i & (1 << j): g1.append(j)
            else: g2.append(j)
        if g1 and g2 and check(g1, g2):
            sig = 1
            cnt1, cnt2 = 0, 0
            for node in g1: cnt1 += P[node]
            for node in g2: cnt2 += P[node]
            res = abs(cnt1 - cnt2)
            if min_dif > res: min_dif = res
            if min_dif == 0: break

    if sig: print(min_dif)
    else: print(-1)

main()