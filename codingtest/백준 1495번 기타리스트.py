import sys
input = sys.stdin.readline

def main():
    n, s, m = map(int, input().split())
    v = list(map(int, input().split()))
    pre = [0] * (m + 1)
    pre[s] = 1
    for i in range(n):
        tmp = [0] * (m + 1)
        for j in range(m + 1):
            if pre[j]:
                if j + v[i] <= m: tmp[j + v[i]] = 1
                if j - v[i] >= 0: tmp[j - v[i]] = 1
        pre = tmp
    for i in range(m, -1, -1):
        if pre[i]:
            return i
    return -1

print(main())