import sys

def solution():
    tc = int(sys.stdin.readline())
    for _ in range(tc):
        n = int(sys.stdin.readline())
        print('Good' if (n + 1) % (n % 100) == 0 else 'Bye')
        
solution()