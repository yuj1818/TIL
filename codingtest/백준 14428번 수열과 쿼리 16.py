import sys, io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Segment:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [(10 ** 9, 10 ** 9)] * (self.n * 2)
        for i in range(self.n):
            self.tree[self.n + i] = (arr[i], i + 1)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, i, v):
        i += self.n
        self.tree[i] = (v, i - self.n + 1)
        i >>= 1
        while i:
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])
            i >>= 1

    def query(self, l, r):
        l += self.n
        r += self.n
        res = (10 ** 9, 10 ** 9)
        while l <= r:
            if l % 2:
                res = min(res, self.tree[l])
                l += 1
            l //= 2
            if not r % 2:
                res = min(res, self.tree[r])
                r -= 1
            r //= 2
        return res[1]

n = int(input())
arr = list(map(int, input().split()))
tree = Segment(arr)
m = int(input())
for _ in range(m):
    d, i, j = map(int, input().split())
    if d == 1: tree.update(i - 1, j)
    else: sys.stdout.write(str(tree.query(i - 1, j - 1)) + '\n')