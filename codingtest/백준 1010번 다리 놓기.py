from math import factorial
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(int(factorial(M)/(factorial(M - N) * factorial(N))))
