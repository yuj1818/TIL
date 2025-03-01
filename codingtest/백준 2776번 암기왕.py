import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        _ = input()
        a = set(input().strip().split())
        _ = input()
        for x in input().strip().split():
            sys.stdout.write(('1' if x in a else '0') + '\n')

if __name__ == '__main__':
    main()