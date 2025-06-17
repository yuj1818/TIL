def calc(v):
    a = [v[i] + v[(i + 1) % 4] + v[(i + 2) % 4] +  v[(i + 3) % 4] for i in range(4)]
    return min(a)

def main():
    n = calc(''.join(open(0).readline().strip().split()))
    ans = 0
    for i in range(1111, int(n) + 1):
        i = str(i)
        if '0' in i: continue
        if calc(i) == i: ans += 1
    print(ans)

main()