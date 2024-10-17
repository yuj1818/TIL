import sys
input = sys.stdin.readline

def main():
    n = int(input())
    limits = list(map(int, input().split()))
    limits.sort()
    i, cnt = 0, 0
    while i < n:
        i += limits[i]
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()