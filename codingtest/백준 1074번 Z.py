dx = [1, -1, 1]
dy = [0, 1, 0]
def div_group(sr, sc, scale, start_value):
    # 4분할 탐색
    if sr + scale > r >= sr and sc + scale > c >= sc:
        # scale이 2가 되면 z 방향 탐색해서 r, c와 일치하는 곳 값 찾아서 return
        if scale == 2:
            if r == sr and c == sc:
                print(start_value)
                return
            for d in range(3):
                nr = sr + dy[d]
                nc = sc + dx[d]
                start_value += 1
                if nr == r and nc == c:
                    print(start_value)
                    return
                sr = nr
                sc = nc
        else:
            div_group(sr, sc, scale // 2, start_value)
            div_group(sr, sc + scale // 2, scale // 2, start_value + (scale ** 2) // 4)
            div_group(sr + scale // 2, sc, scale // 2, start_value + ((scale ** 2) // 4) * 2)
            div_group(sr + scale // 2, sc + scale // 2, scale // 2, start_value + ((scale ** 2) // 4) * 3)

N, r, c = map(int, input().split())
div_group(0, 0, 2 ** N, 0)
