import sys
input = sys.stdin.readline
diff = [
    [0, 4, 3, 3, 4, 3, 2, 2, 1, 2, 6],
    [4, 0, 5, 3, 2, 5, 6, 2, 5, 4, 2],
    [3, 5, 0, 2, 5, 4, 3, 5, 2, 3, 5],
    [3, 3, 2, 0, 3, 2, 3, 3, 2, 1, 5],
    [4, 2, 5, 3, 0, 3, 4, 2, 3, 2, 4],
    [3, 5, 4, 2, 3, 0, 1, 3, 2, 1, 5],
    [2, 6, 3, 3, 4, 1, 0, 4, 1, 2, 6],
    [2, 2, 5, 3, 2, 3, 4, 0, 3, 2, 4],
    [1, 5, 2, 2, 3, 2, 1, 3, 0, 1, 7],
    [2, 4, 3, 1, 2, 1, 2, 2, 1, 0, 6],
    [6, 2, 5, 5, 4, 5, 6, 4, 7, 6, 0]
]

for _ in range(int(input())):
    a, b = map(lambda x: list(map(int, x)), input().strip().split())
    la, lb = len(a), len(b)
    if la > lb: b = [10] * (la - lb) + b
    elif lb > la: a = [10] * (lb - la) + a
    ans = 0
    for i in range(len(a)):
        ans += diff[a[i]][b[i]]
    print(ans)