t = 0
for _ in range(5):
    n = int(input())
    if n >= 40: t += n
    else: t += 40
print(t // 5)