n = int(input())
checked = [0] * 2000002
checked[n] = 1
q = [(n, 0)]
while q:
    x, cnt = q.pop(0)
    if x == 1:
        print(cnt)
        break
    for nx, sig in [(x + 1, 0), (x - 1, 0), (x // 2, x % 2), (x // 3, x % 3)]:
        if checked[nx] or sig: continue
        checked[nx] = 1
        q.append((nx, cnt + 1))
