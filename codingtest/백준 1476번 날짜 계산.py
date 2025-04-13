e, s, m = map(int, open(0).readline().split())
x = s
while (x - e) % 15 != 0 or (x - m) % 19 != 0:
    x += 28
print(x)