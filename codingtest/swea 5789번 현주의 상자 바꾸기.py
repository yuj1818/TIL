T = int(input())

for testcase in range(T):
    N, Q = map(int, input().split())
    lr_list = [list(map(int, input().split())) for _ in range(Q)]
    boxes = [0] * N
    
    for i in range(Q):
        l, r = lr_list[i]
        boxes[l - 1: r] = [i + 1] * (r - l + 1)
    print(f"#{testcase+1} {' '.join(map(str, boxes))}")
