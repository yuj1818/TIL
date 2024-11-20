import sys
input = sys.stdin.readline
n = int(input())
cnt = {}
for _ in range(n):
    title = input()
    cnt[title] = cnt.get(title, 0) + 1
print(sorted(cnt.items(), key= lambda x: (-x[1], x[0]))[0][0])