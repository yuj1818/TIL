import sys, heapq
input = sys.stdin.readline
n = int(input())
lectures = []
for _ in range(n):
    s, f = map(int, input().split())
    heapq.heappush(lectures, (f, s))
ans = 1
last = heapq.heappop(lectures)[0]
while lectures:
    now = heapq.heappop(lectures)
    if last <= now[1]:
        ans += 1
        last = now[0]
print(ans)