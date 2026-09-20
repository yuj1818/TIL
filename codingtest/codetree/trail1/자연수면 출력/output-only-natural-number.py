a, b = map(int, input().split())
if a > 0: print(''.join(map(str, [a for _ in range(b)])))
else: print(0)