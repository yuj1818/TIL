import sys
input = sys.stdin.readline
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def spring():
    global ans
    for y in range(n):
        for x in range(n):
            if tree[y][x]:
                ntree = dict()
                dead = 0
                isValid = True
                for age in sorted(tree[y][x].keys()):
                    cnt = tree[y][x][age]
                    if land[y][x] >= age * cnt:
                        land[y][x] -= age * cnt
                        ntree[age + 1] = ntree.get(age + 1, 0) + cnt
                    elif isValid:
                        isValid = False
                        possible = land[y][x] // age
                        dead += (cnt - possible) * (age // 2)
                        ans -= cnt - possible
                        if possible:
                            land[y][x] -= possible * age
                            ntree[age + 1] = ntree.get(age + 1, 0) + possible
                    else:
                        dead += cnt * (age // 2)
                        ans -= cnt
                tree[y][x] = ntree
                land[y][x] += dead
            land[y][x] += a[y][x]

def fall():
    global ans
    for y in range(n):
        for x in range(n):
            ntree = 0
            for age in tree[y][x].keys():
                if age % 5 == 0: ntree += tree[y][x][age]
            if ntree:
                for dy, dx in d:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n:
                        tree[ny][nx][1] = tree[ny][nx].get(1, 0) + ntree
                        ans += ntree

n, m, k = map(int, input().split())
land = [[5] * n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
tree = [[dict() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    y, x, z = map(int, input().split())
    tree[y - 1][x - 1][z] = tree[y - 1][x - 1].get(z, 0) + 1
ans = m
for _ in range(k):
    spring()
    fall()
print(ans)