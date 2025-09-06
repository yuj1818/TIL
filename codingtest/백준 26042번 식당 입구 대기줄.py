from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
ans = [0, n]
for _ in range(n):
    a, *b = map(int, input().split())
    if a == 1:
        q.append(b[0])
        l = len(q)
        if l > ans[0]: ans = [len(q), b[0]]
        elif l == ans[0]: ans[1] = min(b[0], ans[1])
    else:
        if q: q.popleft()
print(*ans)