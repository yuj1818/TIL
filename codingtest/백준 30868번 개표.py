import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print('++++ ' * (n // 5) + '|' * (n % 5))

if __name__ == '__main__':
    main()