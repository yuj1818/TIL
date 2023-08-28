T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    min_v = 1000    # 포장 별 최소 개수 차이
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if carrots[i] != carrots[i + 1] and carrots[j] != carrots[j + 1]: # 같은 크기의 당근은 무조건 같은 상자에 들어가야 함
                s = i + 1       # 소 상자에 들어간 당근 개수
                m = j - i       # 중 상자에 들어간 당근 개수
                l = N - 1 - j   # 대 상자에 들어간 당근 개수
                if s <= N // 2 and m <= N // 2 and l <= N // 2:
                    if min_v > max(s, m, l) - min(s, m, l):
                        min_v = max(s, m, l) - min(s, m, l)
    if min_v == 1000:
        min_v = -1
    print(min_v)
