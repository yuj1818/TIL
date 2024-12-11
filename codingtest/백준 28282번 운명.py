import sys

def main():
    x, k, *a = map(int, sys.stdin.read().split())
    l, r = [0] * k, [0] * k
    ans = x ** 2
    for i in range(2 * x):
        if i < x: l[a[i] - 1] += 1
        else: r[a[i] - 1] += 1
    for i in range(k): ans -= l[i] * r[i]
    print(ans)

main()