from collections import deque
import sys
input = sys.stdin.readline
ans = set()
for _ in range(int(input())):
    w = input().rstrip()
    if w in ans: continue
    s = deque(w)
    for _ in range(1, len(s)):
        s.rotate()
        if ''.join(s) in ans: break
    else: ans.add(''.join(s))
print(len(ans))
