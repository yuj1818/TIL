from collections import deque
cur = input()
f, b = deque(), deque()
for _ in range(int(input())):
    v = input().split()
    op = int(v[0])
    if op == 1:
        f.append(v[1])
    elif op == 2:
        b.appendleft(v[1])
    elif op == 3:
        if f:
            b.appendleft(cur)
            cur = f.pop()
    else:
        if b:
            f.append(cur)
            cur = b.popleft()
    print(f"{f[-1] if f else '(Null)'} {cur} {b[0] if b else '(Null)'}")
    
