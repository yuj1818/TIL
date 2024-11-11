import sys
input = sys.stdin.readline

def main():
    n = int(input())
    towers = list(map(int, input().split()))
    s = []
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        h = towers[i]
        while s:
            idx, v = s.pop()
            if h >= v:
                ans[idx] = i + 1
            else:
                s.append((idx, v))
                break
        s.append((i, h))
    print(*ans)

if __name__ == '__main__':
    main()