n = int(input())
a = input()
i, t = 0, 0
while i < len(a):
    j = i + 1
    while j < len(a) and a[j] != ' ':
        j += 1
    t += int(a[i:j])
    i = j + 1
print(t - (n * (n - 1) // 2))