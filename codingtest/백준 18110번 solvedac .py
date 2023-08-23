n = int(input())
opinion = sorted(int(input()) for _ in range(n))
removed_n = round(n * 0.15 + 0.0000001)
opinion = opinion[removed_n:n - removed_n]
try:
    level = round(sum(opinion)/len(opinion) + 0.0000001)
    print(level)
except:
    print(0)