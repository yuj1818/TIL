import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    arr = [-1] * (n + 1)

    def find(n):
        if arr[n] < 0: return n
        arr[n] = find(arr[n])
        return arr[n]

    def union(x, y):
        if x == y: return
        px, py = find(x), find(y)
        if px == py: return
        if arr[px] < arr[py]:
            arr[px] += arr[py]
            arr[py] = px
        else:
            arr[py] += arr[px]
            arr[px] = py

    for _ in range(m):
        f, a, b = map(int, input().split())
        if f:
            print('YES' if find(a) == find(b) else 'NO')
        else:
            if a != b: union(a, b)

main()