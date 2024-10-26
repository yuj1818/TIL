# 재귀 풀이

import sys

def find(n, k):
    if n >= k:
        return n - k
    if n == 0:
        return 1 + find(n + 1, k)
    if k % 2 == 0:
        return min(k - n, find(n, k // 2))
    return 1 + min(find(n, k + 1), find(n, k - 1))

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    print(find(n, k))

# bfs 풀이

from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

if n == k:
    print(0)
elif n > k:
    print(n - k)
else:
    visited = [0] * 100001
    q = deque([(n, 0)])
    ans = int(1e9)

    while q:
        x, t = q.popleft()

        if x == k:
            ans = min(ans, t)
            continue
        
        visited[x] = 1

        if t >= ans:
            continue
        
        for nx, nt in [(x + 1, 1), (x - 1, 1), (2 * x, 0)]:
            if 0 <= nx <= 100000 and not visited[nx]:
                q.append((nx, t + nt))

    print(ans)