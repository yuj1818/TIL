import sys

def check(seq):
    l = len(seq)
    for i in range(1, l // 2 + 1):
        a = seq[l - i:]
        b = seq[l - 2 * i : l - i]
        if a == b: return False
    return True

def solve(cur):
    if len(cur) == n:
        print(cur)
        sys.exit()
    for x in ['4', '5', '6']:
        nxt = cur + x
        if check(nxt): solve(nxt)

n = int(input())
solve('')
