import sys
input = sys.stdin.readline

def check(code):
    is_v = 0
    for i in range(len(code)):
        if vowels.get(code[i]):
            is_v = 1
        if i > 0:
            if code[i] == code[i-1] and code[i] != 'e' and code[i] != 'o':
                return False
        if i > 1:
            va, vb, vc = [vowels.get(x) for x in code[i-2:i+1]]
            if va and vb and vc:
                return False
            if not va and not vb and not vc:
                return False
    return is_v

vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
while True:
    code = input().rstrip()
    if code == 'end':
        break
    print('<{}> is {}.'.format(code, 'acceptable' if check(code) else 'not acceptable'))