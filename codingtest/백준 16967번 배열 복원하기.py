import sys
input = sys.stdin.readline

def main():
    h, w, x, y = map(int, input().split())
    B = [list(map(int, input().split()))[:w] for _ in range(h)]
    for i in range(h - x):
        for j in range(w - y):
            B[x + i][y + j] -= B[i][j]
    for row in B:
        print(' '.join(map(str, row)))

main()