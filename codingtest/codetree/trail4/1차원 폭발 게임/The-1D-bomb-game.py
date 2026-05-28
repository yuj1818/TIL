n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
exploded = True
while exploded and numbers:
    exploded = False
    tmp = [numbers[0]]
    cnt = 1
    for i in range(1, n):
        if numbers[i] == tmp[-1]:
            cnt += 1
            tmp.append(numbers[i])
        else:
            if cnt >= m:
                n -= cnt
                for _ in range(cnt): tmp.pop()
                exploded = True
            cnt = 1
            tmp.append(numbers[i])
    if cnt >= m:
        n -= cnt
        for _ in range(cnt): tmp.pop()
        exploded = True
    numbers = tmp
print(n)
print('\n'.join(map(str, numbers)))