from sys import stdin
N, M = map(int, stdin.readline().strip().split())
pocketmon = ['']
for i in range(1, N + 1):
    pocketmon.append(stdin.readline().strip())
for _ in range(M):
    prob = stdin.readline().strip()
    if prob.isdigit():
        print(pocketmon[int(prob)])
    else:
        print(pocketmon.index(prob))