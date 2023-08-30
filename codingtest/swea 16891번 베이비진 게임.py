T = int(input())
def is_run(c):
    for num in c:
        if c.count(num) == 3:
            return True

def is_triplet(c):
    for num in c:
        if num + 1 in c and num + 2 in c:
            return True

def find_winner():
    c1 = []
    c2 = []
    for i in range(0, 12, 2):
        c1.append(cards[i])
        if i >= 4:
            if is_run(c1) or is_triplet(c1):
                return 1
        c2.append(cards[i + 1])
        if i >= 4:
            if is_run(c2) or is_triplet(c2):
                return 2
    return 0

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    print(f'#{tc} {find_winner()}')