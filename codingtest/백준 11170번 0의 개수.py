import sys, math
input = sys.stdin.readline

def f(n):
    if n < 0: return 0
    if n == 0: return 1
    res, L = 1, int(math.log10(n) + 1)
    a = [1] + [10 ** i for i in range(1, L)]
    for i in range(1, L):
        if (n % a[i]) // a[i - 1] == 0: res += ((n - a[i]) // a[i]) * a[i - 1] + n % a[i - 1] + 1
        else: res += (n // a[i]) * a[i - 1]
    return res

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(f(m) - f(n - 1))
