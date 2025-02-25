input = open(0).readline

def main():
    n, m, l, k = map(int, input().split())
    stars = []
    ans = 0
    for _ in range(k):
        stars.append(tuple(map(int, input().split())))
    for x, y in stars:
        scr = sorted([r for c, r in stars if x <= c <= x + l])
        s = 0
        for e in range(len(scr)):
            while scr[e] - scr[s] > l:
                s += 1
            if ans < (e - s + 1): ans = e - s + 1
    print(k-ans)

main()