import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = dict()

    def add(self, a):
        cur = self.root
        for f in a:
            if f not in cur: cur[f] = dict()
            cur = cur[f]
        cur[0] = True

    def search(self, d, cur):
        if 0 in cur: return
        child = sorted(cur)
        for c in child:
            print('--' * d + c)
            self.search(d + 1, cur[c])

n = int(input())
arr = []
data = Trie()
for _ in range(n):
    _, *a = input().strip().split()
    data.add(a)
data.search(0, data.root)