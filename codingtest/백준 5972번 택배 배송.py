import sys, heapq
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    dist = [1e9] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, node = heapq.heappop(pq)
        for nxt, c in graph[node]:
            if dist[nxt] > d + c:
                dist[nxt] = d + c
                heapq.heappush(pq, (dist[nxt], nxt))
    print(dist[n])

if __name__ == '__main__':
    main()