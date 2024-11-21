import sys
input = sys.stdin.readline
INF = int(1e9)

def bis(n, liquid):
    l1, l2 = 0, 0
    l, r = 0, n - 1
    mn = 2 * INF
    while l < r:
        v = liquid[r] + liquid[l]
        if v > 0:
            if v < mn:
                mn = v
                l1, l2 = liquid[l], liquid[r]
            r -= 1
        else:
            if -v < mn:
                mn = -v
                l1, l2 = liquid[l], liquid[r]
            l += 1
    print(l1, l2)

n = int(input())
liquid = list(map(int, input().split()))
bis(n, liquid)