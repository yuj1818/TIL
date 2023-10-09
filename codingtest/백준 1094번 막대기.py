import heapq
X = int(input())
sticks = [64]
while sum(sticks) > X:
    stick = heapq.heappop(sticks) // 2
    if stick + sum(sticks) < X:
        heapq.heappush(sticks, stick)
    heapq.heappush(sticks, stick)
print(len(sticks))
