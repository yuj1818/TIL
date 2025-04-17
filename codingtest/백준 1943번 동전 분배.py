import sys
input = sys.stdin.readline

def check():
    n = int(input())
    coin = []
    total = 0
    for _ in range(n):
        v, c = map(int, input().split())
        coin.append((v, c))
        total += v * c
    if total % 2 == 1: return 0
    total //= 2
    coin.sort(key=lambda x: -x[1])
    money = {0}
    for v, c in coin:
        if v > total: return 0
        tmp = set()
        for m in money:
            for i in range(1, c + 1):
                x = m + v * i
                if x == total: return 1
                if x > total or x in money: break
                tmp.add(x)
        money.update(tmp)
    return 0

def main():
    for _ in range(3): sys.stdout.write(f'{check()}\n')

main()