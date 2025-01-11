import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    ans = 0
    arr.sort()
    i, j = 0, n - 1
    while i < j:
        s = arr[i] + arr[j]
        if s <= x:
            if s == x: ans += 1
            i += 1
        else: j -= 1
    print(ans)

main()