priority = {'+': 0, '*': 1}
def change_f(f, N):
    stack = []
    start = 0
    formula = ''
    while start < N:
        if start == N - 1:
            formula += f[start]
            while stack:
                formula += stack.pop()
        elif f[start].isdigit():
            formula += f[start]
        else:
            if stack:
                while stack and priority[stack[-1]] >= priority[f[start]]:
                    formula += stack.pop()
            stack.append(f[start])
        start += 1
    return formula

def calculate(formula):
    stack = []
    for c in formula:
        if c.isdigit():
            stack.append(int(c))
        else:
            a, b = stack.pop(), stack.pop()
            if c == '*':
                stack.append(a * b)
            else:
                stack.append(a + b)
    return stack.pop()

for tc in range(1, 11):
    N = int(input())
    f = input()
    answer = calculate(change_f(f, N))
    print(f'#{tc} {answer}')