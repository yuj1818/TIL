T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    weights = sorted(q, reverse=True)
    idx_list = [i for i in range(N)]
    for i in range(N):
        while q[i] < max(q[i:]):
            q.append(q.pop(i))
            idx_list.append(idx_list.pop(i))
    print(idx_list.index(M) + 1)