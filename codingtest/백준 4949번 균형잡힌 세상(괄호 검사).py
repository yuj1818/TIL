pair = {']': '[', ')': '('}
while True:
    s = input()
    if s == '.':
        break
    stack = []
    sig = 0
    for c in s:
        if c in pair.values():
            stack.append(c)
        elif c in pair.keys():
            if stack and stack[-1] == pair[c]:
                stack.pop()
            else:
                sig = 1
                break
    if stack or sig:
        print('no')
    else:
        print('yes')