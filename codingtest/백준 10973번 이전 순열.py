import sys

input = sys.stdin.readline


def find():
    i = n - 2
    while i >= 0 and p[i] <= p[i + 1]:
        i -= 1
    if i < 0:
        return -1
    j = n - 1
    while p[i] <= p[j]:
        j -= 1
    p[i], p[j] = p[j], p[i]
    p[i + 1 :] = p[i + 1 :][::-1]
    return ' '.join(map(str, p))


n = int(input())
p = list(map(int, input().split()))
print(find())
