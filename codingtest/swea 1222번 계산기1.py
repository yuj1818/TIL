for tc in range(1, 11):
    N = int(input())
    f = input()
    formula = f[0]
    stack = []
    for i in range(1, len(f)):
        if f[i].isdigit():
            formula += f[i] + stack.pop()
        else:
            stack.append(f[i])
    nums = []
    answer = 0
    for c in formula:
        if c.isdigit():
            nums.append(int(c))
        else:
            while nums:
                answer += nums.pop()
    print(f'#{tc} {answer}')