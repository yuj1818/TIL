def dfs(depth, N, stack, s):
    global min_sum
    if depth == N:
        min_sum = min(s, min_sum)
        return

    for i in range(N):
        if i in stack:
            continue
        if s + arr[depth][i] > min_sum:
            continue
        stack.append(i)
        dfs(depth + 1, N, stack, s + arr[depth][i])
        stack.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    min_sum = 9 * N
    dfs(0, N, stack, 0)
    print(f'#{tc} {min_sum}')