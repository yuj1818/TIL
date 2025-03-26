from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    juwel = defaultdict(list)
    for _ in range(n):
        m, v = list(map(int, input().split()))
        juwel[m].append(v)
    c = sorted([int(input()) for _ in range(k)])
    jw = sorted(juwel.keys(), reverse=True)
    ans = 0
    hq = []
    for x in c:
        while jw and jw[-1] <= x:
            m = jw.pop()
            for v in juwel[m]: heappush(hq, -v)
        if hq: ans -= heappop(hq)
    print(ans)

main()