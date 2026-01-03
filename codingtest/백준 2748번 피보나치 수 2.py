n = int(input())
a = [-1] * (n + 1)
a[0], a[1] = 0, 1

def f(n):
    if a[n] > -1: return a[n]
    a[n] = f(n - 1) + f(n - 2)
    return a[n]

print(f(n))