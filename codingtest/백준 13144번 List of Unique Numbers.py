import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    check = [0] * 1000001
    s, e = 0, 0
    ans = 0
    while s <= e and e < n:
        if not check[a[e]]:
            check[a[e]] = 1
            e += 1
            ans += e - s
        else:
            check[a[s]] = 0
            s += 1
    print(ans)
main()