import sys
input = sys.stdin.readline
n, m = map(int, input().split())
song = []
for _ in range(n):
    t, s, *a = input().strip().split()
    song.append([s, ''.join(a)])
for _ in range(m):
    ans = []
    q = input().strip().replace(' ', '')
    for i in range(n):
        if song[i][1][:3] == q: ans.append(song[i][0])
    v = len(ans)
    if v > 1: print('?')
    elif v == 1: print(ans[0])
    else: print('!')