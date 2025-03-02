import sys
input = sys.stdin.readline
a = [int(input()) for _ in range(int(input()))]
sys.stdout.write('\n'.join(map(str, sorted(a, reverse=True))))