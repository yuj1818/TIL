import sys
input = sys.stdin.readline

def calc(a):
    mr = 0
    nl = []
    for i, row in enumerate(a):
        tmp = dict()
        for x in row:
            if x == 0: continue
            if tmp.get(x): tmp[x] += 1
            else: tmp[x] = 1
        arr = []
        for k, v, in sorted(tmp.items(), key=lambda x: (x[1], x[0])):
            if k: arr.extend([k, v])
        l = len(arr)
        if mr < l: mr = l
        nl.append(arr)
    na = [[0] * mr for _ in range(len(nl))]
    for i in range(len(nl)):
        for j in range(len(nl[i])):
            if j >= 100: break
            na[i][j] = nl[i][j]
    return na

def main():
    r, c, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(3)]
    ans = 0
    rl, cl = len(a), len(a[0])
    while ans < 101:
        if 0 <= r - 1 < rl and 0 <= c - 1 < cl and a[r - 1][c - 1] == k: break
        if rl >= cl: a = calc(a)
        else: a = list(zip(*calc(list(zip(*a)))))
        ans += 1
        rl, cl = len(a), len(a[0])
    print(ans if ans < 101 else -1)

main()