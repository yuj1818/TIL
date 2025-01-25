import sys
sys.setrecursionlimit(10**6)

def find(n):
    if arr[n] == n: return n
    arr[n] = find(arr[n])
    return arr[n]

def union(x, y, i):
    px, py = find(x), find(y)
    if px > py:
        arr[py] = px
    elif py > px:
        arr[px] = py
    else:
        print(i)
        sys.exit()

n, m = map(int, sys.stdin.readline().split())
arr = list(range(n))
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b, i + 1)
print(0)