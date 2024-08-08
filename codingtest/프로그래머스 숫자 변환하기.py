from collections import deque

def solution(x, y, n):
    q = deque([(x, 0)])
    visited = [0] * (y + 1)
    while q:
        v, cnt = q.popleft()
        if v == y:
            return cnt
            
        for num in [v + n, v * 2, v * 3]:
            if y >= num and not visited[num]:
                q.append((num, cnt + 1))
                visited[num] = 1
    return -1