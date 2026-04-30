def find_max(idx):
    global ans
    if idx == n:
        l, r = 0, 0
        for s, e in selected:
            if r < s: l, r = s, e
            else: break
        else:
            ans = max(ans, len(selected))
        return
    
    selected.append(lines[idx])
    find_max(idx + 1)
    selected.pop()
    find_max(idx + 1)

n = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(n)])
ans = 0
selected = list()
find_max(0)
print(ans)
