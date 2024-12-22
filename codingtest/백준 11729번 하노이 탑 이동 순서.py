import sys

def hanoi(i, s, e, v):
    k = (i, s, e, v)
    if k in memo: return memo[k]
    if i == 1: return f'{s} {e}'
    res = '\n'.join([hanoi(i - 1, s, v, e), f'{s} {e}', hanoi(i - 1, v, e, s)])
    memo[k] = res
    return res

n = int(sys.stdin.readline())
memo = dict()
print((1 << n) - 1)
print(hanoi(n, 1, 3, 2))