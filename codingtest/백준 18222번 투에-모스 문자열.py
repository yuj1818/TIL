def find(n):
    if n == 0: return 0
    if n == 1: return 1
    if n % 2 == 0: return find(n // 2)
    return 1 - find(n // 2)

print(find(int(input()) - 1))