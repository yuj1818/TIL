import sys
input = sys.stdin.readline

limit = {'Y': 1, 'F': 2, 'O': 3}
n, g = input().split()
print(len(set(input() for _ in range(int(n)))) // limit[g])