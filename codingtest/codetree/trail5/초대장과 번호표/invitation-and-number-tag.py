n, g = map(int, input().split())
invited = [0] * n
groups = [set() for _ in range(g)]
included = [[] for _ in range(n)]
ans = 0
for i in range(g):
    sz, *group = list(map(int, input().split()))
    for x in group:
        groups[i].add(x - 1)
        included[x - 1].append(i)
q = [0]
invited[0] =1 
while q:
    x = q.pop(0)
    ans += 1
    for gi in included[x]:
        groups[gi].remove(x)
        if len(groups[gi]) == 1:
            nx = list(groups[gi])[0]
            if not invited[nx]:
                invited[nx] = 1
                q.append(nx)
print(ans)