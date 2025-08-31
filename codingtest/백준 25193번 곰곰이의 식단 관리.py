n = int(input())
s = input()
print(n // (n - s.count('C') + 1))