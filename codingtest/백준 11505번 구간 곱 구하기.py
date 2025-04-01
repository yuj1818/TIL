import sys, io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Segment:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1 << ((self.n - 1).bit_length())
        self.tree = [1] * (self.size * 2)
        self.tree[self.size:self.size + self.n] = arr
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] * self.tree[i * 2 + 1] % 1000000007

    def __getitem__(self, i):
        return self.tree[i + self.size]

    def update(self, i, x):
        i += self.size
        self.tree[i] = x
        i >>= 1
        while i:
            self.tree[i] = self.tree[i * 2] * self.tree[i * 2 + 1] % 1000000007
            i >>= 1

    def query(self, i, s, e, l, r):
        if r <= s or e <= l: return 1
        if s <= l and r <= e: return self.tree[i]
        mid = (l + r) // 2
        return self.query(i * 2, s, e, l, mid) * self.query(i * 2 + 1, s, e, mid, r) % 1000000007

    def calc(self, s, e):
        return self.query(1, s, e, 0, self.size)

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = Segment(arr)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1: tree.update(b - 1, c)
    else: sys.stdout.write(str(tree.calc(b - 1, c)) + '\n')