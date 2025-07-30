a, b = map(int, input().split())
print(b - a - 1)
for i in range(a + 1, b): print(i, end=' ')