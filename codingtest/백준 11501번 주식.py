import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        costs = list(map(int, input().split()))
        max_price = costs[-1]
        ans = 0
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, costs[i])
            ans += max_price - costs[i]
        print(ans)

if __name__ == "__main__":
    main()