import sys
input = sys.stdin.readline
blocks = [[], [4, 5], [], [4, 5], [2, 3], [8], [2, 3], [8], [6, 7]]
n = 0
while 1:
    n += 1
    c = list(map(int, input().rstrip()))
    if c[0] == 0: break
    if c[0] != 1 or c[-1] != 2:
        print(f'{n}. NOT')
        continue
    for i in range(len(c) - 1):
        if c[i + 1] in blocks[c[i]]: continue
        print(f'{n}. NOT')
        break
    else: print(f'{n}. VALID')