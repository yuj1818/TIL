from functools import cmp_to_key
n = int(input())
s = [input() for _ in range(n)]

def count(b):
    l, res = 0, 0
    for x in b:
        if x == '(': l += 1
        else: res += l
    return res

def cmp(b1, b2):
    return count(b2 + b1) - count(b1 + b2)

s.sort(key=cmp_to_key(cmp))
print(count(''.join(s)))