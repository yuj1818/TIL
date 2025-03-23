import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        a = sorted(map(int, input().split()))
        print(a[-3])

main()