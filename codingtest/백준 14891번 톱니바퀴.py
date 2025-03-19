import sys
input = sys.stdin.readline

def rotate(i, d):
    visited[i] = 1
    l, r = i - 1, i + 1
    if 0 <= l and not visited[l] and gears[l][2] != gears[i][-2]: rotate(l, -d)
    if r < 4 and not visited[r] and gears[r][-2] != gears[i][2]: rotate(r, -d)
    if d == 1: gears[i] = gears[i][-1] + gears[i][:-1]
    else: gears[i] = gears[i][1:] + gears[i][0]

def main():
    global gears, visited
    gears = [input().strip() for _ in range(4)]
    for _ in range(int(input())):
        idx, d = map(int, input().split())
        visited = [0] * 4
        rotate(idx - 1, d)

    ans = 0
    for i in range(4):
        if int(gears[i][0]): ans += 2 ** i
    print(ans)

main()