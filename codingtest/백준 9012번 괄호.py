T = int(input())
for _ in range(T):
    s = input()
    stack = []
    sig = True
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                sig = False
    if sig:
        if stack:
            ans = "NO"
        else:
            ans = "YES"
    else:
        ans = "NO"

    print(ans)