from sortedcontainers import SortedSet
n, k = map(int, input().split())
arr = SortedSet(map(int, input().split()))
for i in range(-1, -1 * k - 1, -1):
    print(arr[i], end=' ')