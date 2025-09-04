import sys
input = sys.stdin.readline
ans = []
for i in range(1, 6):
    if 'FBI' in input().strip(): ans.append(str(i))
print('HE GOT AWAY!' if not ans else ' '.join(sorted(ans)))