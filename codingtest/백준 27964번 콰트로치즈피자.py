import sys
input()
T = list(input().rstrip().split())
S = set()
for t in T:
    if t.endswith('Cheese'):
        S.add(t)
        if len(S) >= 4:
            print('yummy')
            sys.exit()
print('sad')