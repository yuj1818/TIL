from itertools import combinations
T = int(input())
def change_pos(cards, cnt):
    if int(''.join(cards)) in changed[cnt]:
        return
    else:
        changed[cnt].append(int(''.join(cards)))

    if cnt == N:
        return
    for i, j in comb_lst:
        cards[i], cards[j] = cards[j], cards[i]
        change_pos(cards, cnt + 1)
        cards[i], cards[j] = cards[j], cards[i]

for tc in range(1, T + 1):
    cards, N = input().split()
    N = int(N)
    cards = list(cards)
    comb_lst = list(combinations(range(len(cards)), 2))
    changed = [[] for _ in range(N + 1)]
    change_pos(cards, 0)
    ans = max(changed[-1])
    print(f'#{tc} {ans}')