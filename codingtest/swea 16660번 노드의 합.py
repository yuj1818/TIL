T = int(input())
def reversed(s):
    if s % 2:
        tree[s // 2] = tree[s] + tree[s - 1]
        if s // 2 == L:
            return
        s -= 2
    else:
        tree[s // 2] = tree[s]
        if s // 2 == L:
            return
        s -= 1
    reversed(s)
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        n_node, n = map(int, input().split())
        tree[n_node] = n
    reversed(N)
    print(f'#{tc} {tree[L]}')