n, l, h = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)[(l if l > 0 else None):(-h if h > 0 else None)]
print(sum(a)/len(a))