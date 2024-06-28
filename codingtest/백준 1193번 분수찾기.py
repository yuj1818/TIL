x = int(input())
i = 1
while x > i: x -= i;i += 1
print('{}/{}'.format(x, i - x + 1) if i % 2 == 0 else '{}/{}'.format(i - x + 1, x))