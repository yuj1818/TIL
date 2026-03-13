import sys

input = sys.stdin.readline
n = int(input())
files = [list(input().split())[:-1] for _ in range(n)]
acc = [''] * n
for i in range(1, max(map(len, files)) + 1):
    for j in range(n):
        acc[j] += files[j][i - 1] if len(files[j]) >= i else '0'
    if len(set(acc)) == n:
        print(i)
        break
