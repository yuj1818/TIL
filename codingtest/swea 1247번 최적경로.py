from itertools import permutations
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    positions = list(map(int, input().split()))
    positions = [(positions[i], positions[i + 1]) for i in range(0, len(positions), 2)]
    company = positions[0]
    home = positions[1]
    clients = positions[2:]
    min_v = 200 * (N + 2)
    for perm in permutations(clients, N):
        sum_v = 0
        start = company
        for client in perm:
            sum_v += abs(client[0] - start[0]) + abs(client[1] - start[1])
            if sum_v > min_v:
                break
            start = client
        sum_v += abs(home[0] - start[0]) + abs(home[1] - start[1])
        min_v = min(min_v, sum_v)
    print(f'#{tc} {min_v}')