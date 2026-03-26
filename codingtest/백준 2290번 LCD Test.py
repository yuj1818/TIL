s, n = map(int, input().split())
def trans(x):
    a = [[' '] * (s + 2) for _ in range(2 * s + 3)]
    for i in range(1, s + 1):
        if x in '02356789': a[0][i] = '-'
        if x in '01234789': a[i][-1] = '|'
        if x in '013456789': a[i + s + 1][-1] = '|'
        if x in '0235689': a[-1][i] = '-'
        if x in '0268': a[i + s + 1][0] = '|'
        if x in '045689': a[i][0] = '|'
        if x in '2345689': a[s + 1][i] = '-'
    return a
ans = [trans(x) for x in str(n)]
for z in zip(*ans):
    for x in z: print(''.join(x), end=' ')
    print()
