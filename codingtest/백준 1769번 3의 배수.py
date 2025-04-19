import sys

def main():
    n = sys.stdin.readline().strip()
    cnt = 0
    while len(n) > 1:
        n = str(sum(int(i)*n.count(i) for i in '123456789'))
        cnt += 1
    print(cnt)
    print('NO' if int(n) % 3 else 'YES')

if __name__ == '__main__':
    main()