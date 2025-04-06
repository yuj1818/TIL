s = input()
n = len(s)
cand = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        cand.append(s[:i + 1][::-1] + s[i + 1:j + 1][::-1] + s[j + 1:][::-1])
print(sorted(cand)[0])