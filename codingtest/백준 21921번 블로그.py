import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

def solution(n, x, visitor):
    s = sum(visitor[:x])
    ans, cnt = s, 1
    for i in range(x, n):
        s += visitor[i] - visitor[i-x]
        if s > ans:
            ans, cnt = s, 1
        elif s == ans:
            cnt += 1
    if ans:
        print(ans)
        print(cnt)
    else:
        print("SAD")

solution(n, x, visitor)