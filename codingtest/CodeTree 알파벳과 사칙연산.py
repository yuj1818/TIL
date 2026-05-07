from itertools import combinations
from collections import deque

def calc(arr):
    f = deque(s)
    v = arr[a_idx[f.popleft()]]
    while f:
        x = f.popleft()
        if x == '-':
            v -= arr[a_idx[f.popleft()]]
        elif x == '+':
            v += arr[a_idx[f.popleft()]]
        elif x == '*':
            v *= arr[a_idx[f.popleft()]]
    return v

s = input()
alpha = []
for x in s:
    if x.isalpha(): alpha.append(x)
alpha = list(alpha)
s_alpha = set(alpha)
a_idx = {x: idx for idx, x in enumerate(s_alpha)}
n = len(s_alpha)
ans = float('-inf')
for comb in set(combinations(list(range(1, 5)) * n, n)):
    ans = max(ans, calc(comb))
print(ans)
