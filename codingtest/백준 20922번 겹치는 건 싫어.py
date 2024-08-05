import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    ans, s = 0, 0
    na = [0]*100001
    for e in range(n):
        na[nums[e]] += 1
        while na[nums[e]] > k:
            na[nums[s]] -= 1
            s += 1
        if e - s + 1 > ans:
            ans = e - s + 1
    print(ans)

if __name__ == '__main__':
    main()