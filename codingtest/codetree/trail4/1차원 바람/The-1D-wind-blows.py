from collections import deque

def move(r, d):
    if d:
        a[r].appendleft(a[r].pop())
    else:
        a[r].append(a[r].popleft())
    if r - 1 >= 0 and not visited[r - 1]:
        for i in range(m):
            if a[r - 1][i] == a[r][i]:
                visited[r - 1] = 1
                move(r - 1, not d)
                break
    if r + 1 < n and not visited[r + 1]:
        for i in range(m):
            if a[r + 1][i] == a[r][i]:
                visited[r + 1] = 1
                move(r + 1, not d)
                break

n, m, q = map(int, input().split())
a = [deque(map(int, input().split())) for _ in range(n)]
winds = [(int(r) - 1, d) for r, d in [input().split() for _ in range(q)]]
for r, d in winds:
    visited = [0] * n
    visited[r] = 1
    move(r, d == 'L')
for row in a:
    print(*row)