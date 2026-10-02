from collections import deque
n = int(input())
rotaries = [deque() for _ in range(4)]
for i in range(n):
    t, p = input().split()
    rotaries[ord(p) - 65].append([i, int(t)])
res = [-1 for _ in range(n)]
nt = 0
while rotaries[0] or rotaries[1] or rotaries[2] or rotaries[3]:
    mt = float('inf')
    cur = [0] * 4
    for d in range(4):
        if not rotaries[d]: continue
        idx, ct = rotaries[d][0]
        mt = min(mt, ct)
        if ct <= nt: cur[d] += 1
    total = sum(cur)
    if total == 4: break
    elif total == 0:
        nt = mt
        continue
    
    for d in range(4):
        if cur[d] and cur[(d - 1) % 4] == 0:
            idx, _ = rotaries[d].popleft()
            res[idx] = nt
    
    nt += 1

print('\n'.join(map(str, res)))