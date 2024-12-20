import sys
input = sys.stdin.readline

def main():
    n = int(input())
    board = list(map(int, input().split()))
    x = int(input())
    unstable = board.count(1)
    s = board.index(1) if unstable > 0 else 0
    if unstable > 2: print('NO')
    elif unstable == 0:
        for i in range(n + 1 - x):
            if board[i] > 2 and board[i + x] >= 1:
                print(f'YES\n{i} {i+x}')
                break
        else: print('NO')
    elif unstable == 1:
        if s - x >= 0 and board[s - x] > 2:
            print(f'YES\n{s-x} {s}')
        elif s + x <= n and board[s + x] >= 1:
            print(f'YES\n{s} {s+x}')
        else: print('NO')
    else:
        if s + x <= n and board[s + x] == 1:
            print(f'YES\n{s} {s+x}')
        else: print('NO')

main()