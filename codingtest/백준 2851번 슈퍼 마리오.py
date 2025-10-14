import sys
input = sys.stdin.readline
scores = [int(input()) for _ in range(10)]
acc = [scores[0]]
for i in range(1, 10):
    x = acc[-1] + scores[i]
    acc.append(x)
    if x >= 100:
        if x - 100 > 100 - acc[-2]: acc.pop()
        break
print(acc[-1])