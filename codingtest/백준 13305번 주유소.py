import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

def solution(n, dist, cost):
    ans, p = 0, cost[0]
    for i in range(n - 1):
        if cost[i] < p:
            p = cost[i]
        ans += p * dist[i]
    print(ans)

solution(n, dist, cost)