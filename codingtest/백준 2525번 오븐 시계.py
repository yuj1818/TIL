h, m = map(int, input().split())
n = int(input())
print(f'{((m + n) // 60 + h) % 24} {(m + n) % 60}')