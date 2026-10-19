from sortedcontainers import SortedSet
C, N = map(int, input().split())
T = SortedSet([int(input()) for _ in range(C)])
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: (x[1], x[0]))
ans = 0
for a, b in AB:
    i = T.bisect_left(a)
    if i >= C: continue
    if T[i] <= b:
        ans += 1
        T.remove(T[i])
        C -= 1
print(ans)