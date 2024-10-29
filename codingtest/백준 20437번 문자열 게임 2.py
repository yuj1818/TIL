import sys
input = sys.stdin.readline

def solution():
    w = input().rstrip()
    k = int(input())
    if k == 1:
        print(1, 1)
        return
    alpha = {chr(i): [] for i in range(97, 123)}
    maxv = -1
    minv = len(w)
    for i, x in enumerate(w):
        alpha[x].append(i)
    for cnt in alpha.values():
        if len(cnt) >= k:
            for i in range(0, len(cnt) - k + 1):
                v = cnt[i + k - 1] - cnt[i] + 1
                if maxv < v: maxv = v
                if minv > v: minv = v
    print(-1 if maxv == -1 else f'{minv} {maxv}')

for _ in range(int(input())):
    solution()