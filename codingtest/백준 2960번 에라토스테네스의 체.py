n, k = map(int, input().split())
a = [1] * (n + 1)
a[0] = a[1] = 0
cnt = 0
for i in range(2, n + 1):
    if a[i]:
        for j in range(i, n + 1, i):
            if a[j]:
                a[j] = 0
                cnt += 1
                if cnt == k:
                    print(j)
                    break
