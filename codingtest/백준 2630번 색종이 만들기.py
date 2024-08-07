import sys

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
w = 0
b = 0

def search(y, x, d):
    global w, b

    pt = paper[y][x]

    for i in range(y, y + d):
        for j in range(x, x + d):
            if pt != paper[i][j]:
                mid = d // 2
                search(y, x, mid)
                search(y + mid , x, mid)
                search(y, x + mid, mid)
                search(y + mid, x + mid, mid)
                return

    if pt:
        b += 1
    else:
        w += 1

search(0, 0, n)

print(w)
print(b)