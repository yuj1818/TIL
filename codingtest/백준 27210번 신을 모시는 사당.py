N = int(input())
stones = list(map(int, input().split()))
r_cnt = 0
l_cnt = 0
dp_l = [0] * N
dp_r = [0] * N
for i in range(N):
    if stones[i] == 1:
        if r_cnt:
            dp_l[i] = max(dp_l[i-r_cnt-1]-r_cnt+1, 1)
        else:
            dp_l[i] = dp_l[i-1] + 1
        r_cnt = 0
        l_cnt += 1
    else:
        if l_cnt:
            dp_r[i] = max(dp_r[i-l_cnt-1]-l_cnt+1, 1)
        else:
            dp_r[i] = dp_r[i-1] + 1
        l_cnt = 0
        r_cnt += 1
print(max(max(dp_r), max(dp_l)))
