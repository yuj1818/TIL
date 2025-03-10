import sys
input = sys.stdin.readline

def main():
    _ = input()
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    d = a - b
    print(len(d))
    print(' '.join(map(str, sorted(d))))

main()