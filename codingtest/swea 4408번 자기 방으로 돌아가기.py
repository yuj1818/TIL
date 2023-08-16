T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * 200
    for _ in range(N):
        d, a = map(int, input().split())
        if d < a:
            for i in range((d + 1) // 2 - 1, (a + 1) // 2):
                visited[i] += 1
        else:
            for i in range((a + 1) // 2 - 1, (d + 1) // 2):
                visited[i] += 1
    print(f'#{tc} {max(visited)}')