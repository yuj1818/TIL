s = '%.300f' % 2 ** (-int(input()))
for i in range(len(s) - 1, 1, -1):
    if s[i] != '0':
        print(s[:i + 1])
        break