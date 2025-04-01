import sys, io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def propagate(i, s, e):
    if lazy[i]:
        tree[i] += (e - s) * lazy[i]
        if i < size:
            lazy[i * 2] += lazy[i]
            lazy[i * 2 + 1] += lazy[i]
        lazy[i] = 0

def update(i, s, e, l, r, d):
    propagate(i, l, r)
    if r <= s or e <= l: return
    if s <= l and r <= e:
        lazy[i] += d
        propagate(i, l, r)
        return
    mid = (l + r) // 2
    update(i * 2, s, e, l, mid, d)
    update(i * 2 + 1, s, e, mid, r, d)
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

def query(i, s, e, l, r):
    propagate(i, l, r)
    if r <= s or e <= l: return 0
    if s <= l and r <= e: return tree[i]
    mid = (l + r) // 2
    return query(i * 2, s, e, l, mid) + query(i * 2 + 1, s, e, mid, r)

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
size = 1 << ((n - 1).bit_length())
tree = [0] * (size * 2)
lazy = [0] * (size * 2)
tree[size:size + n] = arr
for i in range(size - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]
for _ in range(m + k):
    a, b, c, *d = map(int, input().split())
    if a == 1: update(1, b - 1, c, 0, size, d[0])
    else: sys.stdout.write(str(query(1, b - 1, c, 0, size)) + '\n')
