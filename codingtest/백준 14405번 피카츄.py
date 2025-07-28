a = ['pi', 'ka', 'chu']
s = input()
l = len(s)
for x in a: s = s.replace(x, ' ' * len(x))
print('YES' if l * ' ' == s else 'NO')
