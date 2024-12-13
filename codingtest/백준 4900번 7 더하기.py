import sys

def trans(s):
    res = 0
    for i in range(0, len(s), 3):
        res = res * 10 + numd[s[i:i+3]]
    return res

numd = {'063':0, '010':1, '093':2, '079':3, '106':4, '103':5, '119':6, '011':7, '127':8, '107':9}
numl = ['063', '010', '093', '079', '106', '103', '119', '011', '127', '107']
while 1:
    tc = sys.stdin.readline().strip()
    if tc == 'BYE': break
    a, b = tc[:-1].split('+')
    res = trans(a)+trans(b)
    ans = ''
    while res > 0:
        ans = numl[res%10] + ans
        res //= 10
    print(tc+ans)