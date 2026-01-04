isbn = input()
res, x = 0, 0
for i, n in enumerate(isbn):
    if n == '*':
        if i % 2: x = 1
        continue
    res += int(n) * (3 if i % 2 else 1)
if x:
    for i in range(10):
        if not (res + (i * 3)) % 10:
            print(i)
            break
else: print(10 - res % 10)