import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    if m == 0: return 0
    if n == 0: return -1
    coins = list(map(int, input().split()))
    visited = set()
    visited.add(0)
    s = [(0, 0)]
    while s:
        ns = []
        while s:
            x, cnt = s.pop()
            if x == m: return cnt
            for coin in coins:
                nx = x + coin
                if -1000 <= nx <= 1000 and nx not in visited:
                    ns.append((nx, cnt + 1))
                    visited.add(nx)
        s = ns
    return -1

print(main())