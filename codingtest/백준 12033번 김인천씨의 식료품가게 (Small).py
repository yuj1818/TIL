import sys
input = sys.stdin.readline
def main():
    for t in range(int(input())):
        input()
        p = list(map(int, input().split()))
        ans = []
        cnt = {x: 0 for x in p}
        for x in p: cnt[x] += 1
        for x in p:
            if (not x % 3) and cnt[x] and cnt[x * 4 // 3]:
                ans.append(x)
                cnt[x] -= 1
                cnt[x * 4 // 3] -= 1
        print(f"Case #{t + 1}: {' '.join(map(str, ans))}")
if __name__ == '__main__': main()