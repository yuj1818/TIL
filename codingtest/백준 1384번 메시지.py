input = open(0).readline
tc = 1
while 1:
    n = int(input())
    if n == 0: break
    res = [input().strip().split() for _ in range(n)]
    isN = False
    print(f'Group {tc}')
    for i in range(n):
        for j in range(1, n):
            if res[i][j] == 'N':
                isN = True
                print(f'{res[i - j][0]} was nasty about {res[i][0]}')
    if not isN: print('Nobody was nasty')
    tc += 1
    print()