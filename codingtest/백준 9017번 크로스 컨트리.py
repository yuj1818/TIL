import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    players = list(map(int, input().split()))
    nums = {}
    score = {}
    pt = 1
    for player in players:
        if nums.get(player):
            nums[player] += 1
        else:
            nums[player] = 1

    nums = {k: v for k, v in nums.items() if v == 6}

    for player in players:
        if nums.get(player):
            if score.get(player):
                if score[player][-1] < 4:
                    score[player][0] += pt
                elif score[player][-1] == 4:
                    score[player][1] = pt
                score[player][-1] += 1
            else:
                score[player] = [pt, 0, 1]

            pt += 1
    print(sorted(score.items(), key= lambda x: (x[1][0], x[1][1]))[0][0])