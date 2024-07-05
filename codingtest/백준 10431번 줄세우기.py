import sys, heapq
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    ans = 0
    t, *students = map(int, input().split())
    hq = [-students[0]]
    for i in range(1, 20):
        if -hq[0] > students[i]:
            taller = len([x for x in hq if x < -students[i]])
            ans += taller
        heapq.heappush(hq, -students[i])
    print(t, ans)