import sys
input = sys.stdin.readline
score = [10, 8, 6, 5, 4, 3, 2, 1]
arr = sorted([input().strip().split() for _ in range(8)])
r, b = 0, 0
for i in range(8):
    t, c = arr[i]
    if c == 'R': r += score[i]
    else: b += score[i]
if r > b: print('Red')
elif b > r: print('Blue')
else: print('Red' if arr[0][1] == 'R' else 'Blue')