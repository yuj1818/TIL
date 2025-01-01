import sys

def find(cnt, n, k):
    global mt, mcnt
    if mt < cnt: return
    if n == k:
        if mt == cnt:
            mcnt += 1
        elif mt > cnt:
            mt = cnt
            mcnt = 1
        return
    if n > k:
        find(cnt + n - k, k, k)
        return
    if n == 0:
        find(cnt + 1, n + 1, k)
        return
    if k % 2 == 0:
        find(cnt + k - n, n, n)
        find(cnt + 1, n, k // 2)
        return
    find(cnt + 1, n, k + 1)
    find(cnt + 1, n, k - 1)

n, k = map(int, sys.stdin.readline().split())
mt, mcnt = 100001, 0
find(0, n, k)
print(mt, mcnt)