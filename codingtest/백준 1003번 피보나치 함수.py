T = int(input())
f = []
for i in range(41):
    if i == 0:
        f.append([1, 0])
    elif i == 1:
        f.append([0, 1])
    else:
        f.append([f[i - 1][0] + f[i - 2][0], f[i - 1][1] + f[i - 2][1]])

for _ in range(T):
    N = int(input())
    print(*f[N])