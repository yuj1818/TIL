from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    rs = list(zip(*s))
    ns = [sum(s[i]) + sum(rs[i]) for i in range(n)]
    total = sum(ns) // 2
    ans = float('inf')
    for comb in combinations(ns[:-1], n // 2):
        diff = abs(total - sum(comb))
        if diff < ans: ans = diff
    print(ans)

main()