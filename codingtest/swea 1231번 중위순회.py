def inorder_travsersal(s):
    if tree[s]:
        inorder_travsersal(tree[s][0])
    print(word[s], end='')
    if len(tree[s]) > 1:
        inorder_travsersal(tree[s][1])

for tc in range(1, 11):
    N = int(input())
    word = dict()
    tree = dict()
    for _ in range(N):
        info = input().split()
        word[info[0]] = info[1]
        tree[info[0]] = info[2:]
    print(f'#{tc} ', end='')
    inorder_travsersal('1')
    print()