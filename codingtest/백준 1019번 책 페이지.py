def nine(n):
    while n > 0 and n % 10 != 9:
        for x in str(n):
            cnt[int(x)] += pos
        n -= 1
    return n

def main():
    global cnt, pos
    n = int(input())
    cnt = [0] * 10
    pos = 1

    while n > 0:
        n = nine(n)
        if n < 10:
            for i in range(n + 1):
                cnt[i] += pos
        else:
            for i in range(10):
                cnt[i] += (n // 10 + 1) * pos
        cnt[0] -= pos
        n //= 10
        pos *= 10

    print(*cnt)

main()