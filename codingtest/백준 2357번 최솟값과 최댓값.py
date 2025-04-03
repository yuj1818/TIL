import sys, io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    size = 1 << ((n - 1).bit_length())
    tree = [[float('inf'), 0] for _ in range(size * 2)]
    for i in range(size, size + n):
        tree[i] = [arr[i - size]] * 2
    for i in range(size - 1, -1, -1):
        tree[i] = [min(tree[2 * i][0], tree[2 * i + 1][0]), max(tree[2 * i][1], tree[2 * i + 1][1])]
    for _ in range(m):
        a, b = map(int, input().split())
        s = size + a - 1
        e = size + b - 1
        minv = float('inf')
        maxv = 0
        while s <= e:
            if s % 2:
                minv = min(minv, tree[s][0])
                maxv = max(maxv, tree[s][1])
            if not e % 2:
                minv = min(minv, tree[e][0])
                maxv = max(maxv, tree[e][1])
            s = (s + 1) // 2
            e = (e - 1) // 2
        sys.stdout.write(f'{minv} {maxv}\n')

main()