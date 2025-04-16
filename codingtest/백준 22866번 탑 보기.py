import sys
input = sys.stdin.readline

def check(tar):
    res = []
    for i in tar:
        while res and arr[res[-1]] <= arr[i]: res.pop()
        view[i] += len(res)
        if res:
            d = abs(i - res[-1])
            if abs(i - dist[i]) > d: dist[i] = res[-1]
        res.append(i)

n = int(input())
arr = list(map(int, input().split()))
view = [0] * n
dist = [float('inf')] * n
check(range(n))
check(range(n - 1, -1, -1))
for i in range(n): sys.stdout.write(f"{view[i]} {dist[i] + 1 if view[i] else ''}\n")