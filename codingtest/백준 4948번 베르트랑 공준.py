import sys
from bisect import bisect_right

MAX = 123456 * 2


def main():
    s = [1] * (MAX + 1)
    s[0] = s[1] = 0
    for i in range(2, int(MAX**0.5) + 1):
        if s[i]:
            s[i * 2 :: i] = [0] * (MAX // i - 1)
    s = [i for i in range(MAX + 1) if s[i]]
    for n in sys.stdin.readlines():
        n = int(n)
        if n == 0:
            break
        print(bisect_right(s, n * 2) - bisect_right(s, n))


if __name__ == '__main__':
    main()
