from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a = deque(enumerate(map(int, input().split())))
ans = []
while a:
    i, cnt = a.popleft()
    ans.append(i + 1)
    if cnt > 0: a.rotate(-(cnt - 1))
    else: a.rotate(-cnt)
print(' '.join(map(str, ans)))