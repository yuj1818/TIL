from collections import deque
A = deque(input())
n = len(A)
ans = n * 2
for _ in range(n):
    A.rotate(1)
    c, cnt = '', 0
    s = ''
    for x in A:
        if x == c: cnt += 1
        else:
            if c: s += f'{c}{cnt}'
            c, cnt = x, 1
    s += f'{c}{cnt}'
    ans = min(ans, len(s))
print(ans)

