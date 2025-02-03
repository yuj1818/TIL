import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s, p = input().strip().split()
    print(s.count(p) + len(s.replace(p, '')))