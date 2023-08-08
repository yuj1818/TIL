K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

def find_max(arr, start, end):
    global N
    if start <= end:
        mid = (start + end) // 2
        c = 0
        for l in arr:
            c += l // mid
        if c >= N:
            return find_max(arr, mid + 1, end)
        else:
            return find_max(arr, start, mid - 1)
    else:
        return end

print(find_max(lines, 1, max(lines)))