import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
mod = 1000000007
pd = {0: 1, 1: 2}

def pow(x):
    cur = pd.get(x)
    if cur: return cur
    m = x // 2
    l, r = pow(m), pow(x - m)
    pd[x] = (l * r) % mod
    return pd[x]

fs, fe = 0, n - 1
bs, be = 0, n - 1
ft = bt = sum(a)
dif = ans = 0
while fs < fe and bs < be:
    ft -= a[fe]
    bt -= a[bs]
    ans += (bt - ft) * pow(dif)
    fe -= 1
    bs += 1
    dif += 1
print(ans % mod)