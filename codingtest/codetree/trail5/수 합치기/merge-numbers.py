from heapq import heappush, heappop
n = int(input())
hq = []
for x in map(int, input().split()): heappush(hq, x)
cost = 0
while len(hq) > 1:
    a, b = heappop(hq), heappop(hq)
    cost += a + b
    heappush(hq, a + b)
print(cost)