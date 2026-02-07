import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    for _ in range(m):
        input()
        x = n + 1
        for v in map(int, input().split()):
            if v > x:
                print('No')
                sys.exit()
            x = v
    print('Yes')

if __name__ == '__main__': main()