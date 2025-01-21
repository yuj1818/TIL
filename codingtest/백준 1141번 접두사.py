import sys
input = sys.stdin.readline
n = int(input())
words = [input().rstrip() for _ in range(n)]
words.sort(key=lambda x: len(x), reverse=True)
ans = 0
d = set()
for word in words:
    if word not in d:
        ans += 1
        s = ''
        for i in range(len(word)):
            s += word[i]
            d.add(s)
print(ans)