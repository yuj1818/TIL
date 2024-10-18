import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    trans = lambda x: x-65 if x < 97 else x - 97 + 26
    G, S = map(int, input().split())
    w = input().rstrip()
    s = input().rstrip()
    wa, sa, ans, start, end = 0, 0, 0, 0, 0
    for c in w:
        wa += 1 << trans(c)
    while end < S:
        sa += 1 << trans(s[end])

        if end >= G - 1:
            ans += 1 if wa == sa else 0
            sa -= 1 << trans(s[start])
            start += 1

        end += 1
    print(ans)

if __name__ == '__main__':
    main()