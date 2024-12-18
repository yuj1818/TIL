import sys
input = sys.stdin.readline

def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    ans = n + 1
    l, r, tmp = 0, 0, 0
    while r < n:
        tmp += a[r]
        while tmp >= s:
            if r - l + 1 < ans: ans = r - l + 1
            tmp -= a[l]
            l += 1
        r += 1
    print(ans % (n + 1))

main()