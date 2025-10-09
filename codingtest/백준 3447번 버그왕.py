import sys, re
s = sys.stdin.readlines()
for x in s:
    while 1:
        res = re.sub('BUG', '', x)
        if 'BUG' in res: x = res
        else:
            print(res, end='')
            break