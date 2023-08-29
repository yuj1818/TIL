N = int(input())
M = int(input())
wrong_btns = []
if M:
    wrong_btns = input().split()
now_ch = 100
min_push = abs(now_ch - N)
if now_ch == N:
    print(0)
else:
    for replace_ch in map(str, range(1000000)):
        for num in replace_ch:
            if num in wrong_btns:
                sig = True
                break
        else:
            min_push = min(min_push, abs(int(replace_ch) - N) + len(replace_ch))
    print(min_push)