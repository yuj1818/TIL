import sys

def main():
    n = int(sys.stdin.readline())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(round(abs(sum([a[i][0] * a[(i + 1) % n][1] - a[i][1] * a[(i + 1) % n][0] for i in range(n)]) / 2), 1))

main()