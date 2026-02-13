import sys

input = sys.stdin.readline


def main():
    n = int(input())
    ans = [0] * n
    for i in range(n):
        a = list(map(int, input().split()))
        if a.count(0) > 1:
            return -1
        if a[i] != 0:
            return -1
        ans[i] = -sum(a) // 2 + n // 2 + 1
    if len(set(ans)) != n:
        return -1
    return ' '.join(map(str, ans))


if __name__ == '__main__':
    print(main())
