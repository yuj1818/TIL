T = int(input())
def min_heap(s):
    if s > N:
        return
    tree[s] = nums[s]
    n = s
    while tree[n // 2] > tree[n]:
        tree[n // 2], tree[n] = tree[n], tree[n // 2]
        n //= 2
    min_heap(s + 1)

for tc in range(1, T + 1):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    tree = [0] * (N + 1)
    min_heap(1)
    ans = 0
    while N >= 1:
        ans += tree[N // 2]
        N //= 2
    print(f'#{tc} {ans}')