import sys
input = sys.stdin.readline
dyx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def main():
    n, m, k = map(int, input().split())
    fires = [list(map(int, input().split())) for _ in range(m)]
    for _ in range(k):
        pos = dict()
        for y, x, m, s, d in fires:
            dy, dx = dyx[d]
            ny, nx = (y + dy * s) % n, (x + dx * s) % n
            if not pos.get((ny, nx)): pos[(ny, nx)] = []
            pos[(ny, nx)].append((ny, nx, m, s, d))

        fires = []
        for k, v in pos.items():
            if len(v) < 2:
                fires += v
                continue
            sm, ss, sd = 0, 0, 0
            for _, _, m, s, d in v:
                sm += m
                ss += s
                sd += d % 2
            if sm < 5: continue
            nm = sm // 5
            ns = ss // len(v)
            nda = [0, 2, 4, 6] if sd == 0 or sd == len(v) else [1, 3, 5, 7]
            for nd in nda:
                fires.append((k[0], k[1], nm, ns, nd))

    ans = 0
    for fire in fires:
        ans += fire[2]
    print(ans)

if __name__ == '__main__':
    main()