import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    a = input().strip().split()
    cnt = {x: 0 for x in '123'}
    for x in a: cnt[x] += 1
    u, d = map(int, input().split())
    ud = u - cnt['1']
    dd = d - cnt['2']
    if ud < 0 or dd < 0:
        print('NO')
    else:
        a = ''.join(a).replace('1', 'U', cnt['1']).replace('2', 'D', cnt['2']).replace('3', 'U', ud).replace('3', 'D', dd)
        print('YES')
        print(a)

solution()