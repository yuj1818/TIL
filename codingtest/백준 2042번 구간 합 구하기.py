import sys
input = sys.stdin.readline

def add(i, x):
    while i > 0:
        tree[i] += x
        i //= 2

def calc(b, c):
    b += cnt
    c += cnt
    res = 0
    while b <= c:
        if b % 2:
            res += tree[b]
            b += 1
        b //= 2

        if not c % 2:
            res += tree[c]
            c -= 1
        c //= 2
    return res

def main():
    global tree, cnt
    n, m, k = map(int, input().split())
    cnt = 1
    while cnt < n:
        cnt <<= 1
    tree = [0] * (cnt * 2)

    for i in range(n):
        x = int(input())
        add(i + cnt, x)

    cnt -= 1
    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            add(b + cnt, c - tree[b + cnt])
        else: print(calc(b, c))

main()