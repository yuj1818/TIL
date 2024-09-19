import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
s = n * (n ** 2 + 1) / 2

def validation():
    if set([x for line in m for x in line]) == set(range(1, n ** 2 + 1)):
        cr, cl = 0, 0
        for i in range(n):
            if sum(m[i]) != s:
                return 'FALSE'
            cr += m[i][i]
            cl += m[i][n - i - 1]

        if cr != s or cl != s:
            return 'FALSE'

        for v in zip(*m):
            if sum(v) != s:
                return 'FALSE'
    else:
        return 'FALSE'

    return 'TRUE'

print(validation())