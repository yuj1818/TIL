import sys
input = sys.stdin.readline

INF = int(1e9)
tc = int(input())

def bf():
    for i in range(n):
        for j in range(len(ways)):
            now, nxt, cost = ways[j]
            if distance[nxt] > distance[now] + cost:
                distance[nxt] = distance[now] + cost
                if i == n - 1:
                    return True
    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    ways = []
    distance = [INF] * (n + 1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        ways.append([s, e, t])
        ways.append([e, s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        ways.append([s, e, -t])

    print("YES" if bf() else "NO")