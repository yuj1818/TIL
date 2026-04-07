import math
def main():
    n = int(input())
    if n == 0: return 0
    if n == 1: return 1
    return math.ceil(round(math.log(n, 2), 10)) + 1
print(main())
