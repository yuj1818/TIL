def solve():
    s = input()
    prev = -1
    for x in 'UCPC':
        s = s[prev + 1:]
        i = s.find(x)
        if i == -1: return 'I hate UCPC'
        prev = i
    return 'I love UCPC'

print(solve())