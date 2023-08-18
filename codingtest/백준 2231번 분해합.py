N = int(input())
for i in range(1, N):
    if i + sum(list(map(int, str(i)))) == N:
        print(i)
        break
else:
    print(0)