import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rule = []
for _ in range(n):
    l, s = map(int, input().split())
    rule.extend([s] * l)
acc = 0
res = [0]
checked = set()
for _ in range(m):
    l, s = map(int, input().split())
    for i in range(acc, acc + l):
        if (rule[i], s) not in checked and rule[i] < s:
            res.append(s - rule[i])
            checked.add((rule[i], s))
    acc += l
print(max(res))