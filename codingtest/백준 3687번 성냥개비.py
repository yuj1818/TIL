import sys
input = sys.stdin.readline
INF = float('inf')

def main():
    cnt = [INF] * 2 + [1, 7, 4, 2, 6, 8] + [INF] * 93
    for i in range(8, 101):
        for j in range(2, i - 1):
            cnt[i] = min(cnt[i], int(str(cnt[j]) + str(cnt[i - j])))
            if j == 6: cnt[i] = min(cnt[i], int(str(cnt[i - j]) + '0'))
    for _ in range(int(input())):
        n = int(input())
        max_l = n // 2
        max_v = '7'+'1' * (max_l - 1) if n % 2 else '1' * max_l
        sys.stdout.write(f'{cnt[n]} {max_v}\n')

main()