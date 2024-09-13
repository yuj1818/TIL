import sys
input = sys.stdin.readline

n = int(input())
ans = n
for _ in range(n):
    word = input()
    for i in range(0, len(word) - 1):
        if word[i] != word[i + 1] and word[i] in word[i + 1:]:
            ans -= 1
            break

print(ans)