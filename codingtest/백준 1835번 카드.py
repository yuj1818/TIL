from collections import deque
n = int(input())
cards = deque(i for i in range(n))
ans = [0] * n
for i in range(1, n + 1):
    cards.rotate(-i)
    ans[cards.popleft()] = i
print(*ans)