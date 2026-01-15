import sys
input = sys.stdin.readline
VOWEL = {'a', 'e', 'i', 'o', 'u'}
L, C = map(int, input().split())
letters = sorted(input().rstrip().split())

def check(arr):
    v, c = 0, 0
    for x in arr:
        if x in VOWEL: v += 1
        else: c += 1
    if v >= 1 and c >= 2: return True
    else: return False

def dfs(arr):
    if len(arr) == L:
        if check(arr): print(''.join(arr))
        return
    for i in range(len(arr), C):
        if arr[-1] < letters[i]:
            arr.append(letters[i])
            dfs(arr)
            arr.pop()

for i in range(C - L + 1): dfs([letters[i]])