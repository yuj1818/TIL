import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        n = input().rstrip()
        cnt = 0
        while n != '6174':
            n = str(int(''.join(sorted(n, reverse=True))) - int(''.join(sorted(n)))).zfill(4)
            cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()