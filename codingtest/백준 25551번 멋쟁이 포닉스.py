import sys
input = sys.stdin.readline
mw, mb = map(int, input().split())
tw, tb = map(int, input().split())
pw, pb = map(int, input().split())
c1, c2 = min(mw, tb, pw), min(mb, tw, pb)
if c1 + c2 == 0: print(0)
elif not c1 or not c2: print(1)
else:
    if c1 == c2: print(2 * c1)
    else: print(2 * min(c1, c2) + 1)