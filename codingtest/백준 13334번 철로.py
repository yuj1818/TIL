from heapq import heappush, heappop
import sys, io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        h, o = map(int, input().split())
        arr.append((min(h, o), max(h, o)))
    d = int(input())
    arr = [x for x in arr if x[1] - x[0] <= d]
    arr.sort(key=lambda x: (x[1], x[0]))
    phase = []
    ans = 0
    for s, e in arr:
        heappush(phase, s)
        sp = e - d
        while phase and sp > phase[0]:
            heappop(phase)
        cnt = len(phase)
        if cnt > ans: ans = cnt
    sys.stdout.write(str(ans))

main()