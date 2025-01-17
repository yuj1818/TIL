import sys
input = sys.stdin.readline

def main():
    n = int(input())
    c = list(map(lambda x: 1 / int(x), input().split()))
    ans = 0
    for i in range(1 << n):
        sub = []
        for j in range(n):
            if i & (1 << j):
                sub.append(c[j])
        if 0.99 <= sum(sub) <= 1.01: ans += 1
    print(ans)

main()