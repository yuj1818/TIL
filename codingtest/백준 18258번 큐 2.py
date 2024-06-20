from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ans = deque([])
for _ in range(n):
    c, *n = input().split()
    if c == 'push':
        ans.append(n[0])
    elif c == 'pop':
        print(ans.popleft() if ans else -1)
    elif c == 'size':
        print(len(ans))
    elif c == 'empty':
        print(0 if ans else 1)
    elif c == 'front':
        print(ans[0] if ans else -1)
    else:
        print(ans[-1] if ans else -1)