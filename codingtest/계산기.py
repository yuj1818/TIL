f = '(6+5*(2-8)/2)'
stack = []
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
formula = ''
stack.append(f[0])
start = 1

while stack:
    if f[start].isdigit():
        formula += f[start]
    elif f[start] == ')':
        while stack[-1] != '(':
            formula += stack.pop()
        stack.pop()
    else:
        while isp[stack[-1]] >= icp[f[start]]:
            formula += stack.pop()
        stack.append(f[start])
    start += 1

stack = []
print(formula)
for c in formula:
    if c.isdigit():
        stack.append(int(c))
    else:
        a, b = stack.pop(), stack.pop()
        if c == '+':
            stack.append(b + a)
        elif c == '-':
            stack.append(b - a)
        elif c == '*':
            stack.append(b * a)
        else:
            stack.append(b / a)
print(stack.pop())