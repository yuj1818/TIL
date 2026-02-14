while 1:
    n = int(input())
    if n < 0: break
    a = [['1'], []]
    t = 1
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            a[0].append(str(i))
            a[1].append(str(n // i))
            t += i + n // i
    print(f"{n} = {' + '.join(a[0] + a[1][::-1])}" if t == n else f'{n} is NOT perfect.')