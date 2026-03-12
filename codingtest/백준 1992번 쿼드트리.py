import sys

input = sys.stdin.readline


def trans(sy, sx, size):
    v = arr[sy][sx]
    for i in range(sy, sy + size):
        for j in range(sx, sx + size):
            if arr[i][j] == v:
                continue
            ns = size // 2
            return f"({''.join([trans(y, x, ns) for y, x in [(sy, sx), (sy, sx + ns), (sy + ns, sx), (sy + ns, sx + ns)]])})"
    return str(v)


n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
print(trans(0, 0, n))
