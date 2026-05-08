def choose(cn):
    if cn == n:
        print(' '.join(map(str, pair)))
        return
    for i in range(1, k + 1):
        if cn > 1 and pair[-1] == pair[-2] == i: continue
        pair.append(i)
        choose(cn + 1)
        pair.pop()

k, n = map(int, input().split())
pair = []
choose(0)
