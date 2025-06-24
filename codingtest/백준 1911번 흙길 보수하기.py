import sys
input = sys.stdin.readline

def main():
    n, l = map(int, input().split())
    holes = [list(map(int, input().split())) for _ in range(n)]
    holes.sort()
    cnt = 0
    last = holes[0][0]
    for s, e in holes:
        if last < s: last = s
        diff = e - last
        if diff % l == 0:
            cnt += diff // l
            last = e
        else:
            cnt += diff // l + 1
            last = e + (l - diff % l)
    print(cnt)

main()