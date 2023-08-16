def find_winner(A, B):
    if cards[A] == cards[B]:
        if A > B:
            return B
        else:
            return A
    elif cards[A] == cards[B] + 1 or cards[A] == (cards[B] + 1) % 3:
        return A
    return B

def divide_group(s, e):
    if s == e:
        return s
    A = divide_group(s, (s + e) // 2)
    B = divide_group((s + e) // 2 + 1, e)
    return find_winner(A, B)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    answer = divide_group(0, N - 1) + 1
    print(f'#{tc} {answer}')