import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
stg, cnt = 0, 0
pos = [0] * n
while cnt < k:
    stg += 1
    arr.insert(0, arr.pop())
    pos.pop()
    pos.insert(0, 0)
    pos[-1] = 0
    for i in range(n - 2, 0, -1):
        if pos[i] and not pos[i + 1] and arr[i + 1] > 0:
            pos[i], pos[i + 1] = 0, 1
            arr[i + 1] -= 1
            if arr[i + 1] == 0:
                cnt += 1
    if arr[0] > 0:
        pos[0] = 1
        arr[0] -= 1
        if arr[0] == 0:
            cnt += 1
print(stg)