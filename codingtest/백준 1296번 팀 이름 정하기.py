import sys
input = sys.stdin.readline
name = input().strip()
nl, no, nv, ne = [name.count(x) for x in 'LOVE']
n = int(input())
ans, cnt = '', -1
for _ in range(n):
    tn = input().strip()
    L = tn.count('L') + nl
    O = tn.count('O') + no
    V = tn.count('V') + nv
    E = tn.count('E') + ne
    res = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if cnt < res: ans, cnt = tn, res
    elif cnt == res and tn < ans: ans, cnt = tn, res
print(ans)