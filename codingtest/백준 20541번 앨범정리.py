from heapq import heappush, heappop
import sys
input = sys.stdin.readline

class Reverse:
    def __init__(self, string):
        self.string = string

    def __lt__(self, other):
        return self.string > other.string

    def __repr__(self):
        return self.string

class Album():
    def __init__(self, name, par, root):
        self.name = name
        self.photos = set()
        self.albums = dict()
        self.par = par
        self.root = root
        self.maxAl = list()
        self.minAl = list()
        self.minPh = list()
        self.maxPh = list()

    def mkalb(self, name):
        if self.albums.get(name): return False
        else:
            self.albums[name] = Album(name, self, self if self.root is None else self.root)
            heappush(self.maxAl, Reverse(name))
            heappush(self.minAl, name)
            return True

    def rmAl(self):
        rmal, rmph = 1, len(self.photos)
        for x in list(self.albums.keys()):
            ca, cp = self.albums[x].rmAl()
            rmal += ca
            rmph += cp
            self.albums.pop(x)
        return rmal, rmph

    def rmalb(self, k):
        rmal, rmph = 0, 0
        if k == '0':
            for x in list(self.albums.keys()):
                ca, cp = self.albums[x].rmAl()
                rmal += ca
                rmph += cp
                self.albums.pop(x)
            self.maxAl = list()
            self.minAl = list()
        elif k == '1':
            if self.albums:
                tKey = heappop(self.maxAl).string
                while self.maxAl and tKey not in self.albums:
                    tKey = heappop(self.maxAl).string
                rmal, rmph = self.albums[tKey].rmAl()
                self.albums.pop(tKey)
        elif k == '-1':
            if self.albums:
                tKey = heappop(self.minAl)
                while self.minAl and tKey not in self.albums:
                    tKey = heappop(self.minAl)
                rmal, rmph = self.albums[tKey].rmAl()
                self.albums.pop(tKey)
        else:
            if self.albums.get(k):
                rmal, rmph = self.albums[k].rmAl()
                self.albums.pop(k)
        return rmal, rmph

    def insert(self, name):
        if name in self.photos: return False
        else:
            self.photos.add(name)
            heappush(self.maxPh, Reverse(name))
            heappush(self.minPh, name)
            return True

    def delete(self, k):
        rmph = 0
        if k == '0':
            rmph += len(self.photos)
            self.photos = set()
            self.minPh = list()
            self.maxPh = list()
        elif k == '1':
            if self.photos:
                tKey = heappop(self.maxPh).string
                while self.maxPh and tKey not in self.photos:
                    tKey = heappop(self.maxPh).string
                rmph += 1
                self.photos.remove(tKey)
        elif k == '-1':
            if self.photos:
                tKey = heappop(self.minPh)
                while self.minPh and tKey not in self.photos:
                    tKey = heappop(self.minPh)
                rmph += 1
                self.photos.remove(tKey)
        else:
            if k in self.photos:
                rmph += 1
                self.photos.remove(k)
        return rmph

    def ca(self, k):
        if k == '..':
            return self.par if self.par is not None else self
        elif k == '/':
            return self.root if self.root is not None else self
        else:
            if self.albums.get(k): return self.albums[k]
            else: return self

n = int(input())
album = Album('album', None, None)
cur = album
for _ in range(n):
    d, k = input().strip().split()
    if d == 'mkalb':
        res = cur.mkalb(k)
        if not res: print('duplicated album name')
    elif d == 'rmalb':
        print(*cur.rmalb(k))
    elif d == 'insert':
        res = cur.insert(k)
        if not res: print('duplicated photo name')
    elif d == 'delete':
        print(cur.delete(k))
    else:
        cur = cur.ca(k)
        print(cur.name)