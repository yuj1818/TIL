def postorder_traversal(s):
    if int(s) > N:
        return
    if not tree[s][0].isdigit():
        postorder_traversal(tree[s][1])
        postorder_traversal(tree[s][2])
    formula.append(tree[s][0])

for tc in range(1, 11):
    N = int(input())
    tree = dict()
    formula = []
    for _ in range(N):
        i = input().split()
        tree[i[0]] = i[1:]
    postorder_traversal('1')
    stack = []
    for c in formula:
        if c.isdigit():
            stack.append(int(c))
        else:
            a, b = stack.pop(), stack.pop()
            if c == '+':
                stack.append(a + b)
            elif c == '-':
                stack.append(b - a)
            elif c == '*':
                stack.append(a * b)
            else:
                stack.append(b / a)
    print(f'#{tc} {int(stack.pop())}')