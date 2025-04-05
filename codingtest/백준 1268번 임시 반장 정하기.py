import sys
input = sys.stdin.readline

def main():
    n = int(input())
    total = [[set() for _ in range(10)] for _ in range(5)]
    info = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(5):
            total[j][info[i][j]].add(i)
    ans, mv = 0, 0
    for i in range(n):
        same = set()
        for j in range(5):
            same.update(total[j][info[i][j]])
        cnt = len(same)
        if cnt > mv:
            mv = cnt
            ans = i + 1
    sys.stdout.write(str(ans))

main()