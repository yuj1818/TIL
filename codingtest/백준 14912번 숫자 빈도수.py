import sys

def main():
    n, d = sys.stdin.readline().strip().split()
    ans = 0
    for num in list(map(str, range(1, int(n) + 1))):
        ans += num.count(d)
    print(ans)

main()