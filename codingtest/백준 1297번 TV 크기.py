d, h, w = map(int, input().split())
v = ((d ** 2) / (h ** 2 + w ** 2)) ** 0.5
print(int(h * v), int(w * v))