rev = lambda x: int(x[::-1])
a, b = map(rev, input().split())
print(rev(str(a + b)))