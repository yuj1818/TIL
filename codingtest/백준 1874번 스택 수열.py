n = int(input())
target = [int(input()) for _ in range(n)]
stack = []
answer = []
num = 1
fail = False
for i in range(n):
    while not fail:
        if not stack or target[i] > stack[-1]:
            stack.append(num)
            answer.append('+')
            num += 1
        elif target[i] == stack[-1]:
            stack.pop()
            answer.append('-')
            break
        else:
            fail = True
if fail:
    print('NO')
else:
    print('\n'.join(answer))