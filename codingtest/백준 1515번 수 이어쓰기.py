import sys
n = sys.stdin.readline().rstrip()

def solution(n):
    ans = 0
    i = 0
    while True:
        ans += 1
        for s in str(ans):
            if n[i] == s:
                i += 1
                if i >= len(n):
                    return ans

print(solution(n))