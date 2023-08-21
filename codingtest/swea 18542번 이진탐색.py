T = int(input())
def inorder_traversal(s):
    global cnt
    if s <= N:
        inorder_traversal(s * 2)
        tree[s] = cnt
        cnt += 1
        inorder_traversal(s * 2 + 1)

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    inorder_traversal(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')