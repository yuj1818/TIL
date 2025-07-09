from collections import deque
n = int(input())
q = deque(range(1, n + 1))
while len(q) > 1:
    print(q.popleft(), end=' ')
    q.append(q.popleft())
print(q[0])