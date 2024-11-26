import sys

def game(tc, p):
    cases = [
        [tc[0], tc[4], tc[-1]],
        [tc[3], tc[4], tc[5]],
        [tc[1], tc[4], tc[7]],
        [tc[2], tc[4], tc[6]],
        [tc[0], tc[1], tc[2]],
        [tc[0], tc[3], tc[6]],
        [tc[6], tc[7], tc[-1]],
        [tc[2], tc[5], tc[-1]]
    ]
    
    return cases.count([p]*3)

while 1:
    tc = sys.stdin.readline().strip()
    if tc == 'end': break
    xl = game(tc, 'X')
    ol = game(tc, 'O')
    ans = 0
    if (xl > 0 and ol > 0) or xl > 2 or ol > 2:
        print('invalid')
        continue
    x = tc.count('X')
    o = tc.count('O')
    if xl or ol:
        if xl and x - 1 == o: ans = 1
        elif ol and x == o: ans = 1
    else:
        if '.' not in tc and x - 1 == o: ans = 1
    print('valid' if ans else 'invalid')