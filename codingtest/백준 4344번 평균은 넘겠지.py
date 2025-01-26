for _ in range(int(input())):
    n, *a = list(map(int, input().split()))
    avg = sum(a) / n
    print(f'{(round(len([x for x in a if x > avg]) / n * 100, 3)):.3f}%')